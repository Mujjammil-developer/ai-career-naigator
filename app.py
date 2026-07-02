from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import sqlite3, json
from model import predict_career, get_skill_gap, get_roadmap, ALL_COURSES

app = Flask(__name__)
app.secret_key = "ai_career_secret_2024"
DB = "career.db"

def safe_skills(val):
    if not val or not isinstance(val, str): return []
    return [s.strip() for s in val.split(",") if s.strip()]

def safe_cgpa(val):
    try: return float(val)
    except: return 0.0

def init_db():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT, email TEXT UNIQUE, password TEXT,
        degree TEXT, branch TEXT, cgpa REAL,
        skills TEXT, certifications TEXT,
        projects TEXT, achievements TEXT, interests TEXT,
        internships TEXT, extra_courses TEXT, languages TEXT
    )""")
    # Add new columns if upgrading from old DB
    for col in ["internships","extra_courses","languages"]:
        try: c.execute(f"ALTER TABLE students ADD COLUMN {col} TEXT")
        except: pass
    conn.commit(); conn.close()

def get_student():
    if "student_id" not in session: return None
    conn = sqlite3.connect(DB)
    row = conn.execute("SELECT * FROM students WHERE id=?", (session["student_id"],)).fetchone()
    conn.close()
    if not row: return None
    cols = ["id","name","email","password","degree","branch","cgpa",
            "skills","certifications","projects","achievements","interests",
            "internships","extra_courses","languages"]
    s = dict(zip(cols, row))
    s["skills"]        = safe_skills(s.get("skills",""))
    s["cgpa"]          = safe_cgpa(s.get("cgpa",0))
    s["internships"]   = safe_skills(s.get("internships",""))
    s["extra_courses"] = safe_skills(s.get("extra_courses",""))
    s["languages"]     = safe_skills(s.get("languages",""))
    return s

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/register", methods=["GET","POST"])
def register():
    if request.method == "POST":
        d = request.form
        conn = sqlite3.connect(DB)
        try:
            conn.execute("""INSERT INTO students
                (name,email,password,degree,branch,cgpa,skills,certifications,
                 projects,achievements,interests,internships,extra_courses,languages)
                VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
                (d["name"], d["email"], d["password"],
                 d.get("degree","BTech"), d.get("branch","Computer Science"),
                 safe_cgpa(d.get("cgpa",0)),
                 d.get("skills",""), d.get("certifications",""),
                 d.get("projects",""), d.get("achievements",""),
                 d.get("interests",""), d.get("internships",""),
                 d.get("extra_courses",""), d.get("languages","")))
            conn.commit()
        except sqlite3.IntegrityError:
            conn.close()
            return render_template("register.html", error="Email already registered.", courses=ALL_COURSES)
        conn.close()
        return redirect(url_for("login"))
    return render_template("register.html", courses=ALL_COURSES)

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        conn = sqlite3.connect(DB)
        row = conn.execute("SELECT * FROM students WHERE email=? AND password=?",
            (request.form["email"], request.form["password"])).fetchone()
        conn.close()
        if row:
            session["student_id"] = row[0]
            session["name"] = row[1]
            return redirect(url_for("dashboard"))
        return render_template("login.html", error="Invalid email or password.")
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.clear(); return redirect(url_for("home"))

@app.route("/dashboard")
def dashboard():
    s = get_student()
    if not s: return redirect(url_for("login"))
    careers = predict_career(s["skills"], s["cgpa"], s["degree"], s["branch"])
    top = careers[0] if careers else {"name":"Software Developer","score":0,"icon":"💻"}
    return render_template("dashboard.html", student=s, careers=careers, top_career=top)

@app.route("/careers")
def careers():
    s = get_student()
    if not s: return redirect(url_for("login"))
    career_list = predict_career(s["skills"], s["cgpa"], s["degree"], s["branch"])
    return render_template("careers.html", careers=career_list, my_skills=s["skills"])

@app.route("/skillgap")
def skillgap():
    s = get_student()
    if not s: return redirect(url_for("login"))
    target = request.args.get("target","")
    from upgraded_model import get_careers_for_course
    all_c = list(get_careers_for_course(s["degree"], s["branch"]).keys())
    if not target and all_c: target = all_c[0]
    gap = get_skill_gap(s["skills"], target, s["degree"], s["branch"])
    return render_template("skillgap.html", my_skills=s["skills"],
        missing=gap["missing"], target=target, all_careers=all_c, percent=gap["percent"])

@app.route("/roadmap")
def roadmap():
    s = get_student()
    if not s: return redirect(url_for("login"))
    target = request.args.get("target","Software Developer")
    return render_template("roadmap.html", roadmap=get_roadmap(target), target=target)

# ── EDIT PROFILE ─────────────────────────────────────────────
@app.route("/edit_profile", methods=["GET","POST"])
def edit_profile():
    s = get_student()
    if not s: return redirect(url_for("login"))
    if request.method == "POST":
        d = request.form
        conn = sqlite3.connect(DB)
        conn.execute("""UPDATE students SET
            name=?, degree=?, branch=?, cgpa=?,
            skills=?, certifications=?, projects=?,
            achievements=?, interests=?, internships=?,
            extra_courses=?, languages=?
            WHERE id=?""",
            (d.get("name", s["name"]),
             d.get("degree", s["degree"]),
             d.get("branch", s["branch"]),
             safe_cgpa(d.get("cgpa", s["cgpa"])),
             d.get("skills",""), d.get("certifications",""),
             d.get("projects",""), d.get("achievements",""),
             d.get("interests",""), d.get("internships",""),
             d.get("extra_courses",""), d.get("languages",""),
             session["student_id"]))
        conn.commit(); conn.close()
        return redirect(url_for("dashboard"))
    return render_template("edit_profile.html", student=s, courses=ALL_COURSES)

@app.route("/get_branches")
def get_branches():
    degree = request.args.get("degree","BTech")
    branches = ALL_COURSES.get(degree, [])
    return jsonify(branches)

@app.route("/chatbot")
def chatbot():
    s = get_student()
    if not s: return redirect(url_for("login"))
    return render_template("chatbot.html", student=s)

@app.route("/chat_api", methods=["POST"])
def chat_api():
    msg = request.json.get("message","").lower()
    s = get_student()
    degree = s["degree"] if s else "BTech"
    branch = s["branch"] if s else "Computer Science"

    responses = {
        "salary":       "Salaries vary by field: IT ₹4-15LPA, Medical ₹6-20LPA, Law ₹3-12LPA, MBA ₹6-18LPA fresher. Grows 3x in 5 years with experience.",
        "internship":   "Find internships on Internshala, LinkedIn, Naukri, Glassdoor, AngelList. Apply 3 months before semester break. Your profile + GitHub matters!",
        "certification":"Top certs by field: IT→AWS/Google Cloud, Finance→CFA/CPA, HR→SHRM, Marketing→Google Ads, Law→Bar Exam, Medical→board exams.",
        "project":      f"For {branch} students: Build 2-3 real projects, publish on GitHub, write a blog about it. Judges love practical work over theory.",
        "higher study": "Popular options: MTech/MS (technical), MBA (management), LLM (law), MD/MS (medical), PhD (research). GRE/GMAT/GATE needed for top colleges.",
        "skill":        f"For {branch}: Focus on core technical skills first, then add communication, Excel, and domain-specific tools. Certifications boost your resume.",
        "resume":       "Keep resume to 1 page. Include: Skills, Projects, Internships, Certifications, Achievements. Use action verbs. Tailor it for each job.",
        "gate":         "GATE prep: Start 6 months early. Focus on core subjects. Practice previous papers. Score 600+ for top NITs/IITs. PSU jobs need GATE.",
        "placement":    "Placement tips: CGPA 7+, 2 internships, 3 projects, good communication, DSA practice (for IT), domain knowledge (for others).",
        "edit":         "You can edit your profile anytime! Click 'Edit Profile' in the dashboard to update skills, internships, certifications and more.",
    }
    reply = f"Great question! As a {branch} student, focus on building strong fundamentals, do internships, and build real projects. Your career match score improves as you add more skills to your profile!"
    for key, val in responses.items():
        if key in msg:
            reply = val
            break
    return jsonify({"reply": reply})

if __name__ == "__main__":
    init_db()
    print("\n✅ AI Career Navigator (Upgraded) running at http://localhost:5000\n")
    app.run(debug=True)
