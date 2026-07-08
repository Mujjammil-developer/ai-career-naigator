from flask import Flask, render_template, request, redirect, url_for, session, jsonify, send_from_directory
import sqlite3
from model import predict_career, get_skill_gap, get_roadmap, ALL_COURSES, get_careers_for_course

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
    s = dict(zip(cols, list(row) + [None]*(len(cols)-len(row))))
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
    top = careers[0] if careers else {"name":"Researcher","score":5,"icon":"🔬"}
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
    all_c = list(get_careers_for_course(s["degree"], s["branch"]).keys())
    target = request.args.get("target", all_c[0] if all_c else "")
    gap = get_skill_gap(s["skills"], target, s["degree"], s["branch"])
    return render_template("skillgap.html", my_skills=s["skills"],
        missing=gap["missing"], target=target, all_careers=all_c, percent=gap["percent"])

@app.route("/roadmap")
def roadmap():
    s = get_student()
    if not s: return redirect(url_for("login"))
    all_c = list(get_careers_for_course(s["degree"], s["branch"]).keys())
    target = request.args.get("target", all_c[0] if all_c else "Default")
    return render_template("roadmap.html", roadmap=get_roadmap(target), target=target, all_careers=all_c)

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
            extra_courses=?, languages=? WHERE id=?""",
            (d.get("name",s["name"]), d.get("degree",s["degree"]),
             d.get("branch",s["branch"]), safe_cgpa(d.get("cgpa",s["cgpa"])),
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
    return jsonify(ALL_COURSES.get(degree, []))

@app.route("/chatbot")
def chatbot():
    s = get_student()
    if not s: return redirect(url_for("login"))
    return render_template("chatbot.html", student=s)

# ── Smart Chat Knowledge Base ─────────────────────────────────
CHAT_KB = {
    "Pharmacy": {
        "cert":   "Top certifications for Pharmacy: 1) GCP (Good Clinical Practice) 2) Pharmacovigilance Cert (PvPI) 3) RAC (Regulatory Affairs) 4) Clinical Research Associate (CRA) 5) NABH Quality Standards. These open doors to hospitals, pharma companies and regulatory bodies!",
        "project":"Best projects for Pharmacy: 1) Drug Interaction Checker App 2) Medication Reminder System 3) Pharmacovigilance Database 4) Drug Inventory System 5) Patient Medication History Tracker. Host on GitHub for placements!",
        "salary": "Pharmacy salaries: Hospital Pharmacist ₹2.5–5 LPA, Clinical Research ₹4–8 LPA, Pharma Sales ₹3–6 LPA+incentives, QA/QC ₹3–7 LPA, Regulatory Affairs ₹5–12 LPA. Grows with specialization!",
        "intern": "Pharmacy internships: Apollo/Fortis/Max hospitals for clinical. Sun Pharma, Cipla, Dr. Reddy's, Lupin for industry. Mandatory 500-hour internship during BPharma. Check Internshala and LinkedIn!",
        "career": "Top careers for Pharmacy: 1) Clinical Pharmacist 2) Drug Regulatory Affairs 3) QA Manager 4) Medical Representative 5) Pharmaceutical Researcher 6) Hospital Pharmacist 7) Pharmacovigilance Officer.",
        "higher": "After BPharma: 1) MPharma (Pharmaceutics/Pharmacology/QA) 2) MBA Pharma Management 3) MSc Clinical Research 4) PhD Pharmaceutical Sciences. GPAT exam needed for MPharma in government colleges!",
        "skill":  "Key skills for Pharmacy: HPLC, GC, Spectroscopy, GMP/GLP, Pharmacology, Patient Counseling, Drug Regulatory knowledge, MS Excel, SOP writing. These are what pharma companies hire for!",
    },
    "Law": {
        "cert":   "Top certifications for Law: 1) Bar Council Enrollment (mandatory!) 2) Diploma in Cyber Law 3) ADR Certificate 4) IP Law Certificate 5) GST Practitioner. LLM specialization for advanced practice.",
        "project":"Best projects for Law: 1) Legal Aid Clinic work 2) Moot Court competitions 3) Legal research papers 4) Case brief compilation 5) Draft model contracts. Publish in legal journals for recognition!",
        "salary": "Law salaries: Junior Associate ₹3–8 LPA, Corporate Lawyer ₹6–15 LPA, In-house Counsel ₹8–20 LPA, Public Prosecutor ₹4–8 LPA. Top firms like AZB, Cyril Amarchand pay ₹15–25 LPA freshers!",
        "intern": "Law internships: District/High Courts for litigation. Khaitan & Co, AZB Partners, Cyril Amarchand Mangaldas for corporate law. HRLN for public interest law. Start interning from 2nd year!",
        "career": "Top law careers: 1) Corporate Lawyer 2) Criminal Lawyer 3) Civil Lawyer 4) Legal Advisor 5) Judge/Magistrate 6) Public Prosecutor 7) Legal Analyst 8) Human Rights Lawyer.",
        "higher": "After LLB: 1) LLM in India (NLU/NLS) 2) LLM abroad (Harvard, Oxford) 3) MBA+LLB for corporate 4) PhD in Law 5) Judicial Services Exam. LSAT needed for foreign LLM programs!",
        "skill":  "Key skills for Law: Legal Research (SCC Online, Manupatra), Contract Drafting, Pleadings, Legal Writing, Negotiation, Case Analysis, MS Word. Learn corporate finance if targeting corporate law!",
    },
    "Architecture": {
        "cert":   "Top certifications for Architecture: 1) COA Registration (mandatory!) 2) LEED Green Associate/AP 3) Revit BIM Certification 4) AutoCAD Certified Professional 5) PMP. LEED is highly valued internationally!",
        "project":"Best projects for Architecture: 1) Sustainable Housing Design 2) Urban Renewal Project 3) Heritage Building Documentation 4) Smart Building Design 5) Low-Cost Housing Solution. Enter NASA, HUDCO competitions!",
        "salary": "Architecture salaries: Junior Architect ₹2.5–5 LPA, Interior Designer ₹3–7 LPA, BIM Manager ₹6–12 LPA, Senior Architect ₹10–25 LPA. International opportunities excellent with 5+ years!",
        "intern": "Architecture internships: Morphogenesis, Sanjay Puri Architects, Studio Lotus, CP Kukreja for top firms. CPWD, HUDCO for government. Mandatory 2-year internship before COA registration!",
        "career": "Top architecture careers: 1) Architect 2) Interior Designer 3) Urban Planner 4) BIM Manager 5) Sustainable Architect 6) Construction Project Manager 7) Landscape Architect. Great freelancing scope!",
        "higher": "After BArch: 1) MArch specialization 2) MUP Urban Planning 3) MSc Sustainable Architecture abroad 4) MBA Construction Management. Top: SPA Delhi, CEPT Ahmedabad, AA London, Harvard GSD.",
        "skill":  "Key skills for Architecture: AutoCAD, Revit, SketchUp, 3ds Max, V-Ray, Hand sketching, Model making, BIM, LEED, Structural basics. Strong portfolio matters MORE than marks in this field!",
    },
    "Medicine & Surgery": {
        "cert":   "Key certifications for MBBS: 1) BLS/ACLS (Basic/Advanced Life Support) 2) ATLS 3) USMLE for USA 4) PLAB for UK 5) MRCP/MRCS for UK specialization. Essential for career advancement!",
        "project":"Best projects for Medical students: 1) Clinical Research Case Studies 2) Public Health Survey 3) Research Publications 4) Community Health Camps. Even 1 publication in a peer-reviewed journal is very impressive!",
        "salary": "Doctor salaries: MBBS fresher ₹3–6 LPA, After MD/MS ₹8–20 LPA, Senior Specialist ₹20–50 LPA. UK/US/Australia can earn ₹50 LPA+ after clearing licensing exams. Private practice is unlimited!",
        "intern": "Medical internship: 1-year compulsory rotating internship after MBBS (NMC mandatory). For research: apply to AIIMS, PGI, CMC Vellore. Elective rotations in UK/US hospitals possible in final year!",
        "career": "Top medical careers: 1) General Physician 2) Surgeon (after MS) 3) Medical Researcher 4) Public Health Officer 5) Medical Administrator 6) Healthcare Entrepreneur 7) Medical Writer.",
        "higher": "After MBBS: 1) MD (medical specialties) 2) MS (surgical specialties) 3) DNB (National Board) 4) MHA (Hospital Administration) 5) MBA Healthcare. NEET-PG exam needed. Top: AIIMS, JIPMER, CMC!",
        "skill":  "Key skills for Medical students: Clinical examination, Diagnostic reasoning, Patient communication, EMR systems, Basic surgery, Research methodology, Medical writing, Medical coding (ICD-10).",
    },
    "Commerce": {
        "cert":   "Top certifications for Commerce: 1) CA (most prestigious!) 2) CMA 3) CS (Company Secretary) 4) CFA 5) ACCA (UK) 6) GST Practitioner. CA from Big 4 opens the best opportunities!",
        "project":"Best projects for Commerce: 1) Financial Analysis of listed companies 2) Tax Return simulation 3) Startup Business Plan 4) Stock Market Portfolio Analysis. Use real NSE/BSE public data!",
        "salary": "Commerce salaries: Accountant ₹2.5–5 LPA, CA fresher ₹7–15 LPA, Financial Analyst ₹4–10 LPA, Tax Consultant ₹3–8 LPA. CA from Big 4 (Deloitte, KPMG, PWC, EY) starts ₹8–12 LPA!",
        "intern": "Commerce internships: CA firms for articleship (mandatory for CA). SBI, HDFC, ICICI for banking. Big 4 for audit internships. Stock broking firms for finance. Internshala has many BCom options!",
        "career": "Top careers for Commerce: 1) Chartered Accountant 2) Financial Analyst 3) Tax Consultant 4) Investment Banker 5) Banking Professional 6) Auditor 7) Cost Accountant 8) Company Secretary.",
        "higher": "After BCom: 1) CA/CMA/CS professional courses 2) MBA Finance 3) MCom 4) CFA 5) ACCA UK 6) MS Finance abroad. MBA from IIM after work experience is most sought after!",
        "skill":  "Key skills for Commerce: Tally ERP, MS Excel (advanced!), GST filing, Financial modeling, SAP FI, Accounting principles, Taxation. Excel and Tally are minimum requirements for any finance job!",
    },
    "Psychology": {
        "cert":   "Top certifications for Psychology: 1) RCI Registration (mandatory for clinical!) 2) CBT Certification 3) NLP Practitioner 4) SHRM-CP (for HR) 5) UX Research Certificate (for tech). RCI required for clinical practice!",
        "project":"Best projects for Psychology: 1) Mental Health Awareness Survey 2) Stress Management Workshop 3) Personality Assessment Study 4) Workplace Wellbeing Research 5) Child Development Case Study.",
        "salary": "Psychology salaries: School Counselor ₹2–4 LPA, HR Specialist ₹3–8 LPA, Clinical Psychologist ₹4–10 LPA, UX Researcher ₹5–15 LPA at tech companies! Organizational Psychologist ₹6–15 LPA.",
        "intern": "Psychology internships: Hospitals for clinical, Corporate HR for organizational, Schools for counseling, NGOs for community work, Tech companies for UX research. Need supervised hours for RCI!",
        "career": "Top psychology careers: 1) Clinical Psychologist (MPhil needed) 2) HR Manager 3) School Counselor 4) UX Researcher (tech!) 5) Organizational Psychologist 6) Market Research Analyst 7) Social Worker.",
        "higher": "After BA/BSc Psychology: 1) MA/MSc Psychology 2) MPhil Clinical (required for clinical practice!) 3) MBA HR 4) MSc Organizational Psychology 5) PhD Psychology. MPhil from RCI-approved institutes is most valuable.",
        "skill":  "Key skills for Psychology: Assessment tools (WAIS, MMPI), CBT techniques, SPSS for statistics, Research methodology, Active listening, Report writing. For UX Research: add Figma and Usability testing!",
    },
    "Computer Science": {
        "cert":   "Top certifications for CS: 1) AWS Solutions Architect 2) Google Cloud Professional 3) Azure Fundamentals 4) Meta Android Developer 5) Oracle Java Certified 6) CCNA networking. AWS is most in-demand right now!",
        "project":"Best CS projects: 1) Full Stack Web App (React + Node.js) 2) Android/iOS App 3) ML project on Kaggle 4) REST API with Python Flask 5) E-commerce with payment gateway. Deploy everything on GitHub!",
        "salary": "CS salaries: Service companies ₹3.5–5 LPA, Product companies ₹8–20 LPA, FAANG ₹30–80 LPA! DSA skills determine which bracket you land in. Skills grow salary 30-40% per year at product companies.",
        "intern": "CS internships: Google, Microsoft, Amazon (top tier), Flipkart, Swiggy, Razorpay (startups), TCS, Infosys (service). Apply on LinkedIn and company portals. LeetCode practice helps get shortlisted!",
        "career": "Top CS careers: 1) Software Developer 2) Full Stack Developer 3) Data Engineer 4) DevOps/Cloud Engineer 5) Cybersecurity Analyst 6) Mobile Developer 7) ML Engineer 8) Product Manager.",
        "higher": "After BTech CS: 1) MS abroad (USA/Canada/Germany) 2) MTech IIT/NIT 3) MBA from IIM 4) PhD. GRE for MS — target CMU, Stanford, Georgia Tech. Work 2 years before MBA is recommended.",
        "skill":  "Essential CS skills: DSA (most important!), Programming language deeply (Java/Python/C++), React/Node for web, SQL, Git. Add: System Design, Cloud (AWS), Docker for high packages at product companies!",
    },
    "Mechanical Engineering": {
        "cert":   "Top certifications for Mechanical: 1) SolidWorks CSWA/CSWP 2) AutoCAD Certified Professional 3) ANSYS Certified 4) Six Sigma Green Belt 5) PMP 6) CATIA Certification. SolidWorks + AutoCAD most demanded!",
        "project":"Best Mechanical projects: 1) IoT Machine Health Monitoring 2) Composite Materials Analysis 3) Robotic Arm Design 4) Solar Vehicle 5) Waste Heat Recovery System. Projects with CFD/FEA simulation are highly valued!",
        "salary": "Mechanical salaries: Fresher ₹2.5–5 LPA, Design Engineer ₹4–8 LPA, Automotive Engineer ₹5–12 LPA, Senior Engineer ₹10–20 LPA. PSU jobs (BHEL, ONGC, ISRO) ₹6–10 LPA with great security!",
        "intern": "Mechanical internships: BHEL, HAL, ISRO, DRDO for government. Tata Motors, Mahindra, L&T, Bosch, Cummins for private. GATE score helps PSU internships. Apply in 3rd year on LinkedIn!",
        "career": "Top Mechanical careers: 1) Design Engineer 2) Manufacturing Engineer 3) Automotive Engineer 4) Robotics Engineer 5) Thermal Engineer 6) Aerospace Engineer 7) Production Manager.",
        "higher": "After BTech Mechanical: 1) MTech specialization 2) MS abroad (USA/Germany — Germany is free!) 3) MBA Operations 4) MEng 5) PhD. GATE for MTech, GRE for MS abroad. Great demand in Germany!",
        "skill":  "Key Mechanical skills: AutoCAD (must!), SolidWorks or CATIA, ANSYS simulation, MATLAB, GD&T, Python for automation. Adding IoT or robotics skills dramatically increases your market value!",
    },
    "Civil Engineering": {
        "cert":   "Top certifications for Civil: 1) AutoCAD Civil 3D 2) STAAD Pro Certification 3) PMP 4) LEED Green Associate 5) NICMAR courses 6) Six Sigma. GATE score opens PSU doors like NHAI, RITES, CPWD!",
        "project":"Best Civil projects: 1) Structural Analysis of G+3 Building 2) Traffic Flow Analysis using GIS 3) Water Quality Assessment 4) Sustainable Building Design 5) Smart City Infrastructure Planning.",
        "salary": "Civil salaries: Site Engineer ₹2.5–5 LPA, Structural Engineer ₹4–9 LPA, Project Manager ₹8–20 LPA, PSU Engineer (NHAI/CPWD) ₹6–10 LPA + excellent benefits. Real estate boom means huge demand!",
        "intern": "Civil internships: CPWD, NHAI, PWD for government. L&T Construction, Shapoorji Pallonji for private. Consulting firms: AECOM, Jacobs, Mott MacDonald. On-site experience is most valued by employers!",
        "career": "Top Civil careers: 1) Structural Engineer 2) Construction Project Manager 3) Urban Planner 4) Transportation Engineer 5) Geotechnical Engineer 6) Environmental Engineer 7) Quantity Surveyor.",
        "higher": "After BTech Civil: 1) MTech Structural/Geo/Transportation 2) MS abroad (USA/Germany/Australia) 3) MBA Construction Management 4) NICMAR PGPM 5) PhD. Infrastructure boom = endless opportunities!",
        "skill":  "Key Civil skills: AutoCAD (must!), STAAD Pro or ETABS, MS Project, GIS, IS Codes, BOQ preparation, Excel. Learning BIM (Revit) gives you a big advantage over other candidates right now!",
    },
}

def get_smart_reply(msg, degree, branch, careers_list):
    msg_lower = msg.lower()
    kb = CHAT_KB.get(branch)
    if not kb:
        for key in CHAT_KB:
            if key.lower() in branch.lower() or branch.lower() in key.lower():
                kb = CHAT_KB[key]; break
    top3 = ', '.join(careers_list[:3]) if careers_list else "top careers in your field"

    if any(w in msg_lower for w in ["cert","certif","exam","license","licenc"]):
        return kb["cert"] if kb else f"Look for professional certifications in {branch}. Check NPTEL, Coursera, and professional bodies for recognized certifications."
    elif any(w in msg_lower for w in ["project","build","make","portfolio","github","create"]):
        return kb["project"] if kb else f"Build 2-3 real projects for {branch}. Focus on solving actual problems and document them well on GitHub or a portfolio website."
    elif any(w in msg_lower for w in ["salary","pay","package","lpa","money","earn","income","stipend"]):
        return kb["salary"] if kb else f"Research {branch} salaries on Glassdoor, AmbitionBox, LinkedIn Salary. Entry level in India: ₹3-8 LPA typically, growing with experience."
    elif any(w in msg_lower for w in ["intern","training","articleship","clerkship"]):
        return kb["intern"] if kb else f"Find internships for {branch} on Internshala, LinkedIn, and directly on company career pages. Apply 3 months before your semester break!"
    elif any(w in msg_lower for w in ["career","option","path","scope","become","future","field","job"]):
        return kb["career"] if kb else f"Your top career options as a {branch} student are: {top3}. Add relevant skills to your profile to see better match scores!"
    elif any(w in msg_lower for w in ["higher","master","pg","postgrad","mtech","mba","ms ","llm","md ","gate","gre","abroad","foreign","study after"]):
        return kb["higher"] if kb else f"Research postgraduate options in {branch}. Consider MTech/MS for technical specialization or MBA for management roles."
    elif any(w in msg_lower for w in ["skill","learn","what should","how to","prepare","course","study"]):
        return kb["skill"] if kb else f"Focus on 3-4 core technical skills for {branch}, then add communication and data skills. Use NPTEL and Coursera for online learning!"
    elif any(w in msg_lower for w in ["resume","cv","interview","tip","help","advice"]):
        return f"Resume tips for {branch} students: 1) Keep to 1 page 2) Lead with skills relevant to your target role 3) Show projects with real outcomes 4) Include certifications prominently 5) Use action verbs like 'Designed', 'Developed', 'Analyzed'. Interview tip: Prepare 3-4 project explanations clearly. Your top careers: {top3}."
    elif any(w in msg_lower for w in ["edit","update","profile","add skill"]):
        return "You can update your profile anytime! Click '✏️ Edit Profile' in the top navigation. Add new skills, internships, or courses — your career match score updates automatically!"
    elif any(w in msg_lower for w in ["hi","hello","hey","hii"]):
        return f"Hello! 😊 I'm your AI Career Assistant for {branch} students! I can help with: career options, certifications, projects, internships, salary info, and higher studies. What would you like to know?"
    elif any(w in msg_lower for w in ["thank","thanks","great","good","awesome"]):
        return f"You're welcome! 😊 Keep learning and updating your skills profile for better career matches. All the best for your {branch} journey! Feel free to ask anything anytime."
    else:
        return f"As a {branch} student, your strongest career options are: {top3}. I can give you specific advice about certifications, projects, internships, salary expectations, or higher study options. Just ask me any of those!"

@app.route("/chat_api", methods=["POST"])
def chat_api():
    msg = request.json.get("message","")
    s = get_student()
    degree = s["degree"] if s else "BTech"
    branch = s["branch"] if s else "Computer Science"
    careers_list = list(get_careers_for_course(degree, branch).keys())
    reply = get_smart_reply(msg, degree, branch, careers_list)
    return jsonify({"reply": reply})
@app.route("/sitemap.xml")
def sitemap():
    return '''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
    <url><loc>https://ai-career-navigator.onrender.com/</loc></url>
    <url><loc>https://ai-career-navigator.onrender.com/register</loc></url>
    <url><loc>https://ai-career-navigator.onrender.com/login</loc></url>
    <url><loc>https://ai-career-navigator.onrender.com/dashboard</loc></url>
    <url><loc>https://ai-career-navigator.onrender.com/careers</loc></url>
    <url><loc>https://ai-career-navigator.onrender.com/skillgap</loc></url>
    <url><loc>https://ai-career-navigator.onrender.com/roadmap</loc></url>
    <url><loc>https://ai-career-navigator.onrender.com/chatbot</loc></url>
</urlset>''', 200, {'Content-Type': 'application/xml'}

@app.route("/robots.txt")
def robots():
    return '''User-agent: *
Allow: /
Sitemap: https://ai-career-navigator-b18z.onrender.com/sitemap.xml''', 200, {'Content-Type': 'text/plain'}


if __name__ == "__main__":
    init_db()
    print("\n✅ AI Career Navigator running at http://localhost:5000\n")
    app.run(debug=True)
