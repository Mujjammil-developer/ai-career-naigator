# model.py — Upgraded: All UG & PG courses + Career Prediction

# ── All Courses ──────────────────────────────────────────────
ALL_COURSES = {
    "BTech": [
        "AI & Data Science", "Computer Science", "Information Technology",
        "Electronics & Communication", "Electrical Engineering",
        "Mechanical Engineering", "Civil Engineering", "Chemical Engineering",
        "Biotechnology", "Aerospace Engineering", "Marine Engineering"
    ],
    "BSc": [
        "Computer Science", "Physics", "Chemistry", "Mathematics",
        "Biology", "Biotechnology", "Statistics", "Microbiology",
        "Environmental Science", "Nursing", "Agriculture"
    ],
    "BA": [
        "Economics", "Psychology", "Sociology", "Political Science",
        "English Literature", "History", "Geography", "Philosophy",
        "Journalism & Mass Communication", "Social Work"
    ],
    "BCA": ["Computer Applications"],
    "BCom": ["Commerce", "Accounting & Finance", "Banking & Insurance"],
    "BBA": ["Business Administration", "Marketing", "Human Resources", "Finance"],
    "BArch": ["Architecture"],
    "BPharma": ["Pharmacy"],
    "MBBS": ["Medicine"],
    "BDS": ["Dental Surgery"],
    "LLB": ["Law", "Corporate Law", "Criminal Law"],
    "MTech": [
        "AI & Machine Learning", "Computer Science", "Data Science",
        "VLSI", "Robotics", "Structural Engineering", "Thermal Engineering"
    ],
    "MSc": [
        "Computer Science", "Data Science", "Physics", "Chemistry",
        "Mathematics", "Biotechnology", "Microbiology", "Psychology"
    ],
    "MBA": [
        "General Management", "Marketing", "Finance", "Human Resources",
        "Operations", "Business Analytics", "Entrepreneurship"
    ],
    "MCA": ["Computer Applications", "Cloud Computing", "Cybersecurity"],
    "LLM": ["Constitutional Law", "Corporate Law", "International Law"],
    "MArch": ["Architecture & Urban Design"],
}

# ── Career paths per course ──────────────────────────────────
COURSE_CAREERS = {
    # BTech
    "AI & Data Science": {
        "AI Engineer":              ["Python","TensorFlow","PyTorch","Deep Learning","MLOps","Docker"],
        "Data Scientist":           ["Python","Statistics","Pandas","Scikit-Learn","SQL","NumPy"],
        "ML Engineer":              ["Python","PyTorch","Spark","Airflow","Kubernetes","Docker"],
        "Data Analyst":             ["SQL","Power BI","Tableau","Python","Excel","Statistics"],
        "NLP Engineer":             ["Python","spaCy","HuggingFace","BERT","NLTK","TensorFlow"],
        "Computer Vision Engineer": ["Python","OpenCV","YOLO","PyTorch","CUDA","Deep Learning"],
        "MLOps Engineer":           ["Docker","Kubernetes","MLflow","AWS","Python","CI/CD"],
        "AI Researcher":            ["Python","Research","Mathematics","Deep Learning","Publications","TensorFlow"],
    },
    "Computer Science": {
        "Software Developer":       ["Java","Python","JavaScript","React","Node.js","SQL"],
        "Full Stack Developer":     ["HTML","CSS","JavaScript","React","Node.js","MongoDB"],
        "Backend Developer":        ["Python","Java","SQL","REST APIs","Docker","Microservices"],
        "DevOps Engineer":          ["Docker","Kubernetes","CI/CD","Linux","AWS","Jenkins"],
        "Cybersecurity Analyst":    ["Networking","Linux","Python","Ethical Hacking","Firewalls","SIEM"],
        "Cloud Engineer":           ["AWS","Azure","GCP","Terraform","Docker","Linux"],
        "Mobile Developer":         ["React Native","Flutter","Android","iOS","Java","Kotlin"],
        "Data Engineer":            ["Python","Spark","Kafka","SQL","Airflow","AWS"],
    },
    "Information Technology": {
        "IT Manager":               ["Project Management","Networking","SQL","Leadership","ITIL","Linux"],
        "System Administrator":     ["Linux","Windows Server","Networking","VMware","PowerShell","Security"],
        "Network Engineer":         ["CCNA","Networking","Cisco","Firewalls","TCP/IP","VPN"],
        "Database Administrator":   ["Oracle","MySQL","SQL Server","Backup","Performance Tuning","SQL"],
        "IT Consultant":            ["Business Analysis","ERP","SAP","Communication","Problem Solving","SQL"],
        "Software Tester":          ["Selenium","Manual Testing","JIRA","Python","Automation","API Testing"],
        "UI/UX Designer":           ["Figma","Adobe XD","User Research","Prototyping","CSS","Wireframing"],
    },
    "Mechanical Engineering": {
        "Mechanical Engineer":      ["AutoCAD","SolidWorks","ANSYS","Manufacturing","Thermodynamics","CNC"],
        "Design Engineer":          ["CATIA","SolidWorks","CAD","FEA","GD&T","Materials Science"],
        "Manufacturing Engineer":   ["CNC","Lean Manufacturing","Six Sigma","AutoCAD","Quality Control","CAM"],
        "Automotive Engineer":      ["AutoCAD","MATLAB","Vehicle Dynamics","CAE","NVH","ADAS"],
        "Robotics Engineer":        ["ROS","Python","Arduino","MATLAB","Control Systems","Sensors"],
        "Thermal Engineer":         ["CFD","ANSYS","Heat Transfer","MATLAB","HVAC","Thermodynamics"],
        "Aerospace Engineer":       ["CATIA","CFD","Aerodynamics","MATLAB","Composites","FEA"],
        "Production Manager":       ["ERP","Lean","Six Sigma","Supply Chain","Quality","AutoCAD"],
    },
    "Civil Engineering": {
        "Structural Engineer":      ["AutoCAD","STAAD Pro","ETABS","Structural Analysis","Concrete","Steel"],
        "Construction Manager":     ["MS Project","AutoCAD","Project Management","Cost Estimation","Safety","Contract"],
        "Urban Planner":            ["GIS","AutoCAD","Urban Design","Zoning","Policy","Statistics"],
        "Geotechnical Engineer":    ["Soil Testing","PLAXIS","Foundation Design","AutoCAD","Lab Analysis","Report Writing"],
        "Transportation Engineer":  ["Highway Design","Traffic Analysis","AutoCAD","GIS","Bridge Design","VISSIM"],
        "Environmental Engineer":   ["Water Treatment","EIA","AutoCAD","GIS","Environmental Law","Monitoring"],
        "Surveyor":                 ["Total Station","GPS","AutoCAD","GIS","Leveling","Remote Sensing"],
    },
    "Electronics & Communication": {
        "Embedded Systems Engineer":["C","Embedded C","Arduino","RTOS","Microcontrollers","PCB Design"],
        "VLSI Engineer":            ["Verilog","VHDL","Cadence","Synopsys","RTL Design","FPGA"],
        "RF Engineer":              ["RF Design","Antenna","MATLAB","CST","Signal Processing","Python"],
        "IoT Engineer":             ["Arduino","Raspberry Pi","MQTT","Python","Cloud","Sensors"],
        "Signal Processing Eng":    ["MATLAB","Python","DSP","Communication","Signal Processing","C++"],
        "Telecom Engineer":         ["5G","LTE","Networking","RF","Protocol","Linux"],
        "PCB Design Engineer":      ["Altium","KiCad","PCB Design","Eagle","EMC","Schematic"],
    },
    "Biotechnology": {
        "Biotech Researcher":       ["PCR","Cell Culture","ELISA","Lab Skills","Data Analysis","Research"],
        "Bioinformatics Scientist": ["Python","R","BLAST","Bioinformatics","Genomics","Linux"],
        "Clinical Research Assoc":  ["GCP","Clinical Trials","Regulatory","Data Management","Protocol","SAS"],
        "Quality Control Analyst":  ["HPLC","GC","SOP","GMP","Lab Skills","Documentation"],
        "Bioprocess Engineer":      ["Fermentation","Upstream","Downstream","GMP","Scale-up","Validation"],
        "Genetic Counselor":        ["Genetics","Counseling","Clinical","Lab Skills","Ethics","Communication"],
    },
    "Economics": {
        "Economist":                ["Statistics","R","Econometrics","STATA","Research","Policy Analysis"],
        "Financial Analyst":        ["Excel","Financial Modeling","Bloomberg","CFA","Valuation","SQL"],
        "Policy Analyst":           ["Research","Statistics","STATA","Policy Writing","Economics","Communication"],
        "Data Analyst":             ["SQL","Excel","Power BI","Statistics","Python","Tableau"],
        "Market Research Analyst":  ["SPSS","Survey Design","Statistics","Excel","Report Writing","Communication"],
        "Investment Banker":        ["Financial Modeling","Excel","Valuation","Bloomberg","Communication","CFA"],
    },
    "Psychology": {
        "Clinical Psychologist":    ["CBT","Assessment","Counseling","DSM","Ethics","Research"],
        "HR Manager":               ["Recruitment","HRIS","Labor Law","Communication","Performance Mgmt","Training"],
        "Counselor":                ["Counseling","CBT","Active Listening","Ethics","Case Management","Assessment"],
        "UX Researcher":            ["User Research","Usability Testing","Figma","Survey Design","Analysis","Communication"],
        "Organizational Psychologist":["OD","Training","Assessment","Statistics","Leadership","Change Mgmt"],
    },
    "Law": {
        "Corporate Lawyer":         ["Contract Law","M&A","Company Law","Legal Research","Drafting","Negotiation"],
        "Criminal Lawyer":          ["Criminal Law","Court Practice","Evidence","Legal Research","Advocacy","IPC"],
        "Civil Lawyer":             ["CPC","Property Law","Family Law","Legal Research","Drafting","Advocacy"],
        "Legal Advisor":            ["Legal Research","Compliance","Risk","Contract","Communication","Drafting"],
        "Judge / Magistrate":       ["Legal Knowledge","Judgment Writing","IPC","CPC","Ethics","Research"],
        "Legal Analyst":            ["Legal Research","Data Analysis","Excel","Policy","Writing","Compliance"],
    },
    "Architecture": {
        "Architect":                ["AutoCAD","Revit","SketchUp","Design","Construction","3ds Max"],
        "Interior Designer":        ["AutoCAD","3ds Max","V-Ray","Space Planning","Material Selection","Revit"],
        "Urban Designer":           ["AutoCAD","GIS","Urban Planning","SketchUp","Rhino","Design"],
        "Landscape Architect":      ["AutoCAD","SketchUp","Planting Design","GIS","3ds Max","Sustainability"],
        "Project Manager":          ["MS Project","Construction Mgmt","Contract","AutoCAD","Cost Control","BIM"],
        "BIM Manager":              ["Revit","BIM","Navisworks","AutoCAD","Coordination","Construction"],
    },
    "MBA": {
        "Product Manager":          ["Product Strategy","Agile","User Research","SQL","Data Analysis","Roadmapping"],
        "Marketing Manager":        ["Digital Marketing","SEO","Analytics","Content Strategy","CRM","Social Media"],
        "Financial Manager":        ["Financial Analysis","Excel","SAP","Budgeting","Risk","Forecasting"],
        "HR Manager":               ["Recruitment","HRIS","Labor Law","Training","Performance","Compensation"],
        "Operations Manager":       ["Supply Chain","Lean","Six Sigma","ERP","Process Improvement","Analytics"],
        "Business Analyst":         ["SQL","Excel","Power BI","Requirements","Process Mapping","Agile"],
        "Entrepreneur":             ["Business Planning","Finance","Marketing","Leadership","Networking","Strategy"],
        "Consultant":               ["Strategy","Problem Solving","Excel","PPT","Communication","Analytics"],
    },
    "Commerce": {
        "Chartered Accountant":     ["Accounting","Taxation","Tally","Excel","Audit","GST"],
        "Financial Analyst":        ["Excel","Financial Modeling","Accounting","Bloomberg","Valuation","CFA"],
        "Tax Consultant":           ["Taxation","GST","Income Tax","Tally","Excel","Compliance"],
        "Auditor":                  ["Audit","Accounting","Excel","Risk","Internal Controls","IFRS"],
        "Cost Accountant":          ["CMA","Costing","Excel","ERP","Budgeting","SAP"],
        "Banking Professional":     ["Banking","Finance","Excel","Customer Service","Compliance","Risk"],
    },
    "Nursing": {
        "Clinical Nurse":           ["Patient Care","Clinical Skills","EMR","BLS","ACLS","Documentation"],
        "Nurse Practitioner":       ["Advanced Practice","Diagnosis","Prescribing","Clinical","Research","Leadership"],
        "Healthcare Administrator": ["Healthcare Mgmt","Excel","Policy","Communication","Budget","Quality"],
        "Public Health Nurse":      ["Community Health","Epidemiology","Health Education","Research","Policy","Communication"],
    },
    "Medicine": {
        "Doctor / Physician":       ["Clinical Skills","Diagnosis","Patient Care","Medical Knowledge","EMR","Ethics"],
        "Surgeon":                  ["Surgical Skills","Anatomy","Clinical","Patient Care","Leadership","Research"],
        "Researcher":               ["Research","Statistics","Lab Skills","Publications","Grant Writing","Ethics"],
        "Medical Administrator":    ["Healthcare Mgmt","Policy","Communication","Budget","Leadership","Quality"],
    },
}

# Add default for courses not explicitly listed
DEFAULT_CAREERS = {
    "Software Developer":   ["Programming","Problem Solving","Algorithms","Communication","Teamwork","Git"],
    "Data Analyst":         ["SQL","Excel","Statistics","Communication","Python","Visualization"],
    "Business Analyst":     ["Excel","Communication","Requirements","Process Mapping","SQL","Presentation"],
    "Researcher":           ["Research","Writing","Statistics","Critical Thinking","Domain Knowledge","Ethics"],
    "Consultant":           ["Communication","Problem Solving","Excel","Presentation","Domain Knowledge","Analysis"],
}

def get_careers_for_course(degree, branch):
    """Get relevant career options based on degree and branch."""
    if branch in COURSE_CAREERS:
        return COURSE_CAREERS[branch]
    # Try matching partial branch names
    for key in COURSE_CAREERS:
        if key.lower() in branch.lower() or branch.lower() in key.lower():
            return COURSE_CAREERS[key]
    # MBA always returns MBA careers
    if degree in ["MBA", "BBA"]:
        return COURSE_CAREERS.get("MBA", DEFAULT_CAREERS)
    if degree in ["LLB", "LLM"]:
        return COURSE_CAREERS.get("Law", DEFAULT_CAREERS)
    if degree == "BArch" or degree == "MArch":
        return COURSE_CAREERS.get("Architecture", DEFAULT_CAREERS)
    return DEFAULT_CAREERS

def predict_career(skills, cgpa, degree="BTech", branch="Computer Science"):
    """Score each career based on skill overlap + CGPA."""
    careers = get_careers_for_course(degree, branch)
    skills_lower = [s.strip().lower() for s in skills if s.strip()]
    results = []
    for career, required in careers.items():
        required_lower = [r.lower() for r in required]
        matched = sum(1 for s in skills_lower if s in required_lower)
        base_score = (matched / len(required)) * 100 if required else 0
        cgpa_bonus = min((cgpa - 6.0) * 2, 5) if cgpa >= 6.0 else 0
        final_score = min(round(base_score + cgpa_bonus, 1), 99)
        results.append({
            "name": career,
            "score": final_score,
            "matched": matched,
            "total": len(required),
            "icon": _icon(career)
        })
    results.sort(key=lambda x: x["score"], reverse=True)
    return results

def get_skill_gap(my_skills, target, degree="BTech", branch="Computer Science"):
    """Return missing skills for a target career."""
    careers = get_careers_for_course(degree, branch)
    if target not in careers:
        for c in careers:
            target = c
            break
    required = careers.get(target, [])
    my_lower = [s.strip().lower() for s in my_skills if s.strip()]
    have    = [s for s in required if s.lower() in my_lower]
    missing = [s for s in required if s.lower() not in my_lower]
    pct = round(len(have) / len(required) * 100) if required else 0
    return {"target":target,"have":have,"missing":missing,"percent":pct}

# Generic 6-month roadmaps per career type
ROADMAPS = {
    "AI Engineer": [
        {"month":"Month 1","title":"Python Advanced & DSA",   "topics":["OOP","Algorithms","Data Structures","Git","Linux"]},
        {"month":"Month 2","title":"Machine Learning Core",   "topics":["Regression","Classification","Clustering","Scikit-Learn","Model Eval"]},
        {"month":"Month 3","title":"Deep Learning",           "topics":["Neural Networks","CNNs","RNNs","TensorFlow","PyTorch"]},
        {"month":"Month 4","title":"Projects & Kaggle",       "topics":["2 End-to-End Projects","Kaggle","GitHub Portfolio","Documentation"]},
        {"month":"Month 5","title":"MLOps & Cloud",           "topics":["Docker","MLflow","AWS Basics","Model Deployment","FastAPI"]},
        {"month":"Month 6","title":"Job Ready",               "topics":["Resume Polish","LinkedIn","Mock Interviews","Apply Jobs"]},
    ],
    "Software Developer": [
        {"month":"Month 1","title":"Core Programming",        "topics":["Java/Python","OOP","Data Structures","Algorithms","Git"]},
        {"month":"Month 2","title":"Web Development",         "topics":["HTML","CSS","JavaScript","React","Node.js"]},
        {"month":"Month 3","title":"Backend & Databases",     "topics":["REST APIs","SQL","MongoDB","Docker","Authentication"]},
        {"month":"Month 4","title":"Projects",                "topics":["Full Stack Project","GitHub","Code Review","Testing","Documentation"]},
        {"month":"Month 5","title":"Cloud & DevOps",          "topics":["AWS","CI/CD","Linux","Docker","Deployment"]},
        {"month":"Month 6","title":"Job Ready",               "topics":["Resume","DSA Practice","Mock Interviews","Applications"]},
    ],
    "Mechanical Engineer": [
        {"month":"Month 1","title":"CAD Fundamentals",        "topics":["AutoCAD","SolidWorks","Drawing Standards","2D/3D Modeling","GD&T"]},
        {"month":"Month 2","title":"Analysis Tools",          "topics":["ANSYS","FEA Basics","CATIA","Simulation","Meshing"]},
        {"month":"Month 3","title":"Core Engineering",        "topics":["Thermodynamics","Fluid Mechanics","Manufacturing","Materials","Quality"]},
        {"month":"Month 4","title":"Industry Projects",       "topics":["Design Project","Report Writing","Peer Review","Presentations","Industry Visit"]},
        {"month":"Month 5","title":"Specialization",          "topics":["Choose: Automotive/Robotics/Thermal","Advanced Software","Certification"]},
        {"month":"Month 6","title":"Job Ready",               "topics":["Resume","Core Company Prep","Interview","Campus Placements"]},
    ],
    "Structural Engineer": [
        {"month":"Month 1","title":"Design Software",         "topics":["AutoCAD","STAAD Pro","ETABS Basics","IS Codes","Drawing Reading"]},
        {"month":"Month 2","title":"Structural Analysis",     "topics":["RCC Design","Steel Design","Load Calculations","SAP2000","Foundation"]},
        {"month":"Month 3","title":"Construction Management", "topics":["Project Planning","MS Project","Cost Estimation","Bar Bending","Specifications"]},
        {"month":"Month 4","title":"Field Projects",          "topics":["Site Visit","Lab Testing","Survey","Technical Report","Drawings"]},
        {"month":"Month 5","title":"Certifications",          "topics":["AutoCAD Certification","STAAD Pro Advanced","IS Code Study","GATE Prep"]},
        {"month":"Month 6","title":"Job Ready",               "topics":["Resume","PSU/Private Companies","GATE Exam","Interviews"]},
    ],
    "Corporate Lawyer": [
        {"month":"Month 1","title":"Legal Foundations",       "topics":["Contract Law","Company Law","Legal Research","LexisNexis","Bare Acts"]},
        {"month":"Month 2","title":"Drafting Skills",         "topics":["Contract Drafting","MOUs","NDA","Legal Writing","Pleadings"]},
        {"month":"Month 3","title":"Corporate Law",           "topics":["M&A","Due Diligence","SEBI Regulations","Compliance","Company Law"]},
        {"month":"Month 4","title":"Internship",              "topics":["Law Firm Internship","Court Visits","Client Meetings","Research Memos"]},
        {"month":"Month 5","title":"Specialization",          "topics":["Tax Law / IP Law / Banking Law","Moot Court","Publications"]},
        {"month":"Month 6","title":"Job Ready",               "topics":["Resume","Bar Council Enrolment","Law Firm Applications","Networking"]},
    ],
    "Default": [
        {"month":"Month 1","title":"Foundation Skills",       "topics":["Core Subject Mastery","Communication","Computer Basics","Excel","Soft Skills"]},
        {"month":"Month 2","title":"Technical Skills",        "topics":["Domain Certifications","Online Courses","Coursera/Udemy","Practice Projects"]},
        {"month":"Month 3","title":"Projects",                "topics":["Mini Project","Portfolio Building","GitHub/LinkedIn","Documentation"]},
        {"month":"Month 4","title":"Internship Prep",         "topics":["Resume Building","Cover Letters","LinkedIn Optimization","Mock Interviews"]},
        {"month":"Month 5","title":"Internship",              "topics":["Apply Internships","Networking","Industry Learning","Professional Skills"]},
        {"month":"Month 6","title":"Job Ready",               "topics":["Final Resume","Company Research","Interview Prep","Applications","Offer"]},
    ],
}

def get_roadmap(target):
    for key in ROADMAPS:
        if key.lower() in target.lower() or target.lower() in key.lower():
            return ROADMAPS[key]
    return ROADMAPS["Default"]

def _icon(career):
    icons = {
        "AI Engineer":"🤖","Data Scientist":"🔬","ML Engineer":"⚙️","Data Analyst":"📊",
        "NLP Engineer":"💬","Computer Vision Engineer":"👁️","Software Developer":"💻",
        "Full Stack Developer":"🌐","Backend Developer":"🔧","DevOps Engineer":"🚀",
        "Cybersecurity Analyst":"🔒","Cloud Engineer":"☁️","Mechanical Engineer":"⚙️",
        "Design Engineer":"✏️","Civil Engineer":"🏗️","Structural Engineer":"🏛️",
        "Corporate Lawyer":"⚖️","Criminal Lawyer":"⚖️","Doctor / Physician":"🏥",
        "Architect":"🏛️","Financial Analyst":"💰","HR Manager":"👥",
        "Marketing Manager":"📣","Product Manager":"🎯","Researcher":"🔬",
        "Entrepreneur":"🚀","Consultant":"💼","Business Analyst":"📈",
        "Chartered Accountant":"📒","Nurse":"🏥","Biotech Researcher":"🧬",
    }
    for k, v in icons.items():
        if k.lower() in career.lower():
            return v
    return "🎯"
