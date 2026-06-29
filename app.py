from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3
from model import predict_career, get_skill_gap, get_roadmap

app = Flask(__name__)
app.secret_key = "ai_career_secret_2024"
DB = "career.db"

def safe_skills(val):
    """Always return a clean list from a skills field."""
    if not val or not isinstance(val, str):
        return []
    return [s.strip() for s in val.split(",") if s.strip()]

def safe_cgpa(val):
    """Always return a float CGPA."""
    try:
        return float(val)
    except (TypeError, ValueError):
        return 0.0

def init_db():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT, email TEXT UNIQUE, password TEXT,
            degree TEXT, branch TEXT, cgpa REAL,
            skills TEXT, certifications TEXT,
            projects TEXT, achievements TEXT, interests TEXT
        )
    """)
    c.execute("""
        CREATE TABLE IF NOT EXISTS recommendations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER, career_name TEXT, match_score REAL
        )
    """)
    conn.commit()
    conn.close()

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/register", methods=["GET","POST"])
def register():
    if request.method == "POST":
        d = request.form
        skills = ",".join([s.strip() for s in d.get("skills","").split(",") if s.strip()])
        conn = sqlite3.connect(DB)
        try:
            conn.execute("""
                INSERT INTO students (name,email,password,degree,branch,cgpa,
                skills,certifications,projects,achievements,interests)
                VALUES (?,?,?,?,?,?,?,?,?,?,?)
            """, (d["name"], d["email"], d["password"],
                  d.get("degree","B.Tech"), d.get("branch","AI & DS"),
                  safe_cgpa(d.get("cgpa", 0)),
                  skills,
                  d.get("certifications",""), d.get("projects",""),
                  d.get("achievements",""), d.get("interests","")))
            conn.commit()
        except sqlite3.IntegrityError:
            conn.close()
            return render_template("register.html", error="Email already registered.")
        conn.close()
        return redirect(url_for("login"))
    return render_template("register.html")

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        conn = sqlite3.connect(DB)
        row = conn.execute(
            "SELECT * FROM students WHERE email=? AND password=?",
            (request.form["email"], request.form["password"])
        ).fetchone()
        conn.close()
        if row:
            session["student_id"] = row[0]
            session["name"] = row[1]
            return redirect(url_for("dashboard"))
        return render_template("login.html", error="Invalid email or password.")
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("home"))

@app.route("/dashboard")
def dashboard():
    if "student_id" not in session:
        return redirect(url_for("login"))
    conn = sqlite3.connect(DB)
    row = conn.execute("SELECT * FROM students WHERE id=?", (session["student_id"],)).fetchone()
    conn.close()
    student = {
        "id": row[0], "name": row[1], "email": row[2],
        "degree": row[3] or "B.Tech",
        "branch": row[4] or "AI & DS",
        "cgpa": safe_cgpa(row[5]),
        "skills": safe_skills(row[6]),
        "certifications": row[7] or "",
        "projects": row[8] or "",
        "achievements": row[9] or "",
        "interests": row[10] or ""
    }
    careers = predict_career(student["skills"], student["cgpa"])
    top_career = careers[0] if careers else {"name": "AI Engineer", "score": 0, "icon": "🤖"}
    return render_template("dashboard.html", student=student,
                           careers=careers, top_career=top_career)

@app.route("/careers")
def careers():
    if "student_id" not in session:
        return redirect(url_for("login"))
    conn = sqlite3.connect(DB)
    row = conn.execute("SELECT skills, cgpa FROM students WHERE id=?", (session["student_id"],)).fetchone()
    conn.close()
    skills = safe_skills(row[0])
    cgpa = safe_cgpa(row[1])
    career_list = predict_career(skills, cgpa)
    return render_template("careers.html", careers=career_list, my_skills=skills)

@app.route("/skillgap")
def skillgap():
    if "student_id" not in session:
        return redirect(url_for("login"))
    target = request.args.get("target", "AI Engineer")
    conn = sqlite3.connect(DB)
    row = conn.execute("SELECT skills FROM students WHERE id=?", (session["student_id"],)).fetchone()
    conn.close()
    my_skills = safe_skills(row[0])
    gap = get_skill_gap(my_skills, target)
    all_careers = ["AI Engineer","Data Scientist","ML Engineer",
                   "Data Analyst","NLP Engineer","Computer Vision Engineer"]
    return render_template("skillgap.html", my_skills=my_skills,
                           missing=gap["missing"], target=target,
                           all_careers=all_careers)

@app.route("/roadmap")
def roadmap():
    if "student_id" not in session:
        return redirect(url_for("login"))
    target = request.args.get("target", "AI Engineer")
    plan = get_roadmap(target)
    return render_template("roadmap.html", roadmap=plan, target=target)

@app.route("/chatbot")
def chatbot():
    if "student_id" not in session:
        return redirect(url_for("login"))
    return render_template("chatbot.html")

@app.route("/chat_api", methods=["POST"])
def chat_api():
    msg = request.json.get("message", "").lower()
    responses = {
        "ai engineer":    "To become an AI Engineer: Learn Python → ML → Deep Learning (TensorFlow/PyTorch) → MLOps. Build 3-4 projects and get an internship. Target FAANG or AI startups.",
        "certification":  "Top certifications: Google ML Certificate, AWS ML Specialty, DeepLearning.AI TensorFlow Developer, IBM Data Science on Coursera.",
        "project":        "Build these projects: 1) Resume Classifier (NLP) 2) Stock Price Predictor (LSTM) 3) Image Classifier (CNN) 4) Chatbot (Transformers) 5) End-to-end ML Pipeline.",
        "salary":         "AI Engineer salary in India: ₹6–15 LPA (fresher), ₹15–40 LPA (3+ years). In US: $120k–$200k+.",
        "internship":     "Find internships on: LinkedIn, Internshala, AngelList, company career pages. Apply to Flipkart, Swiggy, startups. Build GitHub portfolio first.",
        "data scientist": "Path: Python + Statistics + SQL → Pandas/NumPy → ML (Scikit-Learn) → Visualization → Kaggle competitions → Projects → Jobs.",
    }
    reply = "Great question! Focus on strong fundamentals in Python and ML, then specialize based on your interests. Keep building projects and contributing to GitHub!"
    for key, val in responses.items():
        if key in msg:
            reply = val
            break
    return {"reply": reply}

if __name__ == "__main__":
    init_db()
    print("\n✅ AI Career Navigator running at http://localhost:5000\n")
    app.run(debug=False)