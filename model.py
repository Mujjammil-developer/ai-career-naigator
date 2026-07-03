# model.py — Complete Career Navigator for ALL UG & PG Students

ALL_COURSES = {
    "BTech": ["AI & Data Science","Computer Science","Information Technology",
              "Electronics & Communication","Electrical Engineering",
              "Mechanical Engineering","Civil Engineering","Chemical Engineering",
              "Biotechnology","Aerospace Engineering","Marine Engineering"],
    "BSc":   ["Computer Science","Physics","Chemistry","Mathematics","Biology",
              "Biotechnology","Statistics","Microbiology","Nursing","Agriculture","Environmental Science"],
    "BA":    ["Economics","Psychology","Sociology","Political Science","English Literature",
              "History","Geography","Philosophy","Journalism & Mass Communication","Social Work"],
    "BCA":   ["Computer Applications","Cloud Computing","Cybersecurity"],
    "BCom":  ["Commerce","Accounting & Finance","Banking & Insurance"],
    "BBA":   ["Business Administration","Marketing","Human Resources","Finance","International Business"],
    "BArch": ["Architecture","Interior Design","Urban Planning"],
    "BPharma":["Pharmacy","Pharmaceutical Sciences","Drug Technology"],
    "MBBS":  ["Medicine & Surgery"],
    "BDS":   ["Dental Surgery"],
    "BVSc":  ["Veterinary Science"],
    "LLB":   ["Law","Corporate Law","Criminal Law","Civil Law"],
    "BEd":   ["Education","Primary Education","Special Education"],
    "BFA":   ["Fine Arts","Visual Arts","Applied Arts"],
    "BHM":   ["Hotel Management","Culinary Arts","Tourism"],
    "MTech": ["AI & Machine Learning","Computer Science","Data Science",
              "VLSI Design","Robotics","Structural Engineering","Thermal Engineering"],
    "MSc":   ["Computer Science","Data Science","Physics","Chemistry",
              "Mathematics","Biotechnology","Microbiology","Psychology","Statistics"],
    "MBA":   ["General Management","Marketing","Finance","Human Resources",
              "Operations","Business Analytics","Entrepreneurship","Healthcare Management"],
    "MCA":   ["Computer Applications","Cloud Computing","Cybersecurity","Software Engineering"],
    "LLM":   ["Constitutional Law","Corporate Law","International Law","Criminal Law"],
    "MArch": ["Architecture & Urban Design","Sustainable Architecture"],
    "MPharma":["Pharmaceutics","Pharmacology","Pharmaceutical Chemistry"],
    "MD":    ["General Medicine","Pediatrics","Cardiology","Dermatology","Psychiatry"],
    "MS":    ["General Surgery","Orthopedics","Ophthalmology","ENT"],
    "MEd":   ["Education Management","Curriculum Design","Special Education"],
    "MFA":   ["Fine Arts","Digital Arts","Sculpture","Painting"],
}

# ── Complete career data for EVERY course ───────────────────
CAREER_DATA = {

    # ── BTECH / MTECH ────────────────────────────────────────
    "AI & Data Science": {
        "AI Engineer":              ["Python","TensorFlow","PyTorch","Deep Learning","MLOps","Docker"],
        "Data Scientist":           ["Python","Statistics","Pandas","Scikit-Learn","SQL","NumPy"],
        "ML Engineer":              ["Python","PyTorch","Spark","Airflow","Kubernetes","Docker"],
        "Data Analyst":             ["SQL","Power BI","Tableau","Python","Excel","Statistics"],
        "NLP Engineer":             ["Python","spaCy","HuggingFace","BERT","NLTK","TensorFlow"],
        "Computer Vision Engineer": ["Python","OpenCV","YOLO","PyTorch","CUDA","Deep Learning"],
        "MLOps Engineer":           ["Docker","Kubernetes","MLflow","AWS","Python","CI/CD"],
        "AI Product Manager":       ["Product Strategy","ML Knowledge","SQL","Communication","Agile","Analytics"],
    },
    "AI & Machine Learning": {
        "AI Researcher":            ["Python","Deep Learning","TensorFlow","Research","Mathematics","Publications"],
        "ML Engineer":              ["Python","PyTorch","Spark","Kubernetes","Docker","MLflow"],
        "Data Scientist":           ["Python","Statistics","Pandas","Scikit-Learn","SQL","NumPy"],
        "AI Engineer":              ["Python","TensorFlow","PyTorch","Deep Learning","MLOps","Docker"],
        "Computer Vision Engineer": ["Python","OpenCV","YOLO","PyTorch","CUDA","Deep Learning"],
        "NLP Engineer":             ["Python","spaCy","HuggingFace","BERT","NLTK","TensorFlow"],
    },
    "Computer Science": {
        "Software Developer":       ["Java","Python","JavaScript","React","Node.js","SQL"],
        "Full Stack Developer":     ["HTML","CSS","JavaScript","React","Node.js","MongoDB"],
        "Backend Developer":        ["Python","Java","SQL","REST APIs","Docker","Microservices"],
        "DevOps Engineer":          ["Docker","Kubernetes","CI/CD","Linux","AWS","Jenkins"],
        "Cybersecurity Analyst":    ["Networking","Linux","Python","Ethical Hacking","Firewalls","SIEM"],
        "Cloud Engineer":           ["AWS","Azure","GCP","Terraform","Docker","Linux"],
        "Mobile App Developer":     ["React Native","Flutter","Android","iOS","Java","Kotlin"],
        "Data Engineer":            ["Python","Spark","Kafka","SQL","Airflow","AWS"],
    },
    "Information Technology": {
        "IT Manager":               ["Project Management","Networking","SQL","Leadership","ITIL","Linux"],
        "System Administrator":     ["Linux","Windows Server","Networking","VMware","PowerShell","Security"],
        "Network Engineer":         ["CCNA","Networking","Cisco","Firewalls","TCP/IP","VPN"],
        "Database Administrator":   ["Oracle","MySQL","SQL Server","Backup","Performance Tuning","SQL"],
        "Software Tester":          ["Selenium","Manual Testing","JIRA","Python","Automation","API Testing"],
        "UI/UX Designer":           ["Figma","Adobe XD","User Research","Prototyping","CSS","Wireframing"],
        "IT Consultant":            ["SAP","ERP","Business Analysis","Communication","SQL","Problem Solving"],
    },
    "Electronics & Communication": {
        "Embedded Systems Engineer":["C","Embedded C","Arduino","RTOS","Microcontrollers","PCB Design"],
        "VLSI Engineer":            ["Verilog","VHDL","Cadence","Synopsys","RTL Design","FPGA"],
        "IoT Engineer":             ["Arduino","Raspberry Pi","MQTT","Python","Cloud","Sensors"],
        "RF Engineer":              ["RF Design","Antenna","MATLAB","Signal Processing","Python","CST"],
        "Telecom Engineer":         ["5G","LTE","Networking","RF","Protocol","Linux"],
        "PCB Design Engineer":      ["Altium","KiCad","PCB Design","Eagle","EMC","Schematic"],
        "Signal Processing Engineer":["MATLAB","Python","DSP","Communication","Signal Processing","C++"],
    },
    "Electrical Engineering": {
        "Electrical Engineer":      ["AutoCAD Electrical","PLC","SCADA","Power Systems","MATLAB","Circuit Design"],
        "Power Systems Engineer":   ["Power Systems","MATLAB","ETAP","Protection","Transformers","Grid"],
        "Automation Engineer":      ["PLC","SCADA","HMI","Robotics","Python","Control Systems"],
        "Control Systems Engineer": ["MATLAB","Simulink","PID","Control Theory","Python","Embedded C"],
        "Solar Energy Engineer":    ["Solar PV","AutoCAD","MATLAB","Power Electronics","Grid Tie","Energy Storage"],
        "Electrical Project Manager":["Project Management","AutoCAD","Power Systems","MS Project","Leadership","Contracts"],
    },
    "Mechanical Engineering": {
        "Mechanical Design Engineer":["AutoCAD","SolidWorks","CATIA","FEA","GD&T","Materials Science"],
        "Manufacturing Engineer":   ["CNC","Lean Manufacturing","Six Sigma","AutoCAD","Quality Control","CAM"],
        "Automotive Engineer":      ["AutoCAD","MATLAB","Vehicle Dynamics","CAE","NVH","ADAS"],
        "Robotics Engineer":        ["ROS","Python","Arduino","MATLAB","Control Systems","Sensors"],
        "Thermal Engineer":         ["CFD","ANSYS","Heat Transfer","MATLAB","HVAC","Thermodynamics"],
        "Aerospace Engineer":       ["CATIA","CFD","Aerodynamics","MATLAB","Composites","FEA"],
        "Production Manager":       ["ERP","Lean","Six Sigma","Supply Chain","Quality","AutoCAD"],
        "Quality Engineer":         ["Six Sigma","SPC","FMEA","ISO 9001","Quality Tools","Metrology"],
    },
    "Civil Engineering": {
        "Structural Engineer":      ["AutoCAD","STAAD Pro","ETABS","Structural Analysis","RCC Design","Steel"],
        "Construction Manager":     ["MS Project","AutoCAD","Project Management","Cost Estimation","Safety","Contract"],
        "Urban Planner":            ["GIS","AutoCAD","Urban Design","Zoning","Policy","Statistics"],
        "Geotechnical Engineer":    ["Soil Testing","PLAXIS","Foundation Design","AutoCAD","Lab Analysis","Report Writing"],
        "Transportation Engineer":  ["Highway Design","Traffic Analysis","AutoCAD","GIS","Bridge Design","VISSIM"],
        "Environmental Engineer":   ["Water Treatment","EIA","AutoCAD","GIS","Environmental Law","Monitoring"],
        "Quantity Surveyor":        ["Estimation","AutoCAD","MS Excel","BOQ","Contract","Rate Analysis"],
        "Site Engineer":            ["AutoCAD","Construction Supervision","Quality Control","Safety","Surveying","Bar Bending"],
    },
    "Chemical Engineering": {
        "Process Engineer":         ["HYSYS","Aspen","Process Design","P&ID","Safety","Chemical Engineering"],
        "Quality Control Engineer": ["HPLC","GC","Lab Skills","GMP","SOP","Documentation"],
        "Petrochemical Engineer":   ["Refinery","HYSYS","Process Safety","Oil & Gas","Chemical Eng","MATLAB"],
        "Environmental Engineer":   ["EIA","Water Treatment","Waste Management","Environmental Law","GIS","Lab Skills"],
        "Research Scientist":       ["Lab Skills","Research","Publications","Chemical Analysis","HPLC","GC-MS"],
        "Safety Engineer":          ["HAZOP","Process Safety","Fire & Gas","OSHA","Risk Assessment","P&ID"],
    },
    "Biotechnology": {
        "Biotech Researcher":       ["PCR","Cell Culture","ELISA","Lab Skills","Data Analysis","Research"],
        "Bioinformatics Scientist": ["Python","R","BLAST","Bioinformatics","Genomics","Linux"],
        "Clinical Research Associate":["GCP","Clinical Trials","Regulatory","Data Management","Protocol","SAS"],
        "Quality Control Analyst":  ["HPLC","GC","SOP","GMP","Lab Skills","Documentation"],
        "Bioprocess Engineer":      ["Fermentation","Upstream","Downstream","GMP","Scale-up","Validation"],
        "Medical Writer":           ["Scientific Writing","Regulatory","MS Word","Research","Communication","Publications"],
        "Regulatory Affairs Officer":["Regulatory","CTD","GMP","FDA","Drug Laws","Documentation"],
    },

    # ── PHARMACY ─────────────────────────────────────────────
    "Pharmacy": {
        "Clinical Pharmacist":      ["Clinical Pharmacy","Drug Interaction","Patient Counseling","Pharmacology","Hospital Pharmacy","EMR"],
        "Pharmaceutical Researcher":["Drug Discovery","Lab Skills","HPLC","Pharmacology","Research","Publications"],
        "Drug Regulatory Affairs":  ["Regulatory","CTD Dossier","FDA/CDSCO","GMP","Drug Laws","Documentation"],
        "Quality Assurance Manager":["GMP","GLP","SOP","Validation","QMS","Audit"],
        "Medical Representative":   ["Pharmacology","Sales","Communication","Product Knowledge","Marketing","CRM"],
        "Hospital Pharmacist":      ["Hospital Pharmacy","Drug Dispensing","Clinical Knowledge","Patient Care","Pharmacology","Inventory"],
        "Pharmaceutical Analyst":   ["HPLC","GC","Spectroscopy","Analytical Chemistry","GLP","Lab Skills"],
        "Production Pharmacist":    ["Manufacturing","GMP","Validation","Process","Documentation","Quality Control"],
    },
    "Pharmaceutical Sciences": {
        "Pharmaceutical Researcher":["Drug Discovery","Lab Skills","HPLC","Pharmacology","Research","Publications"],
        "Clinical Pharmacist":      ["Clinical Pharmacy","Drug Interaction","Patient Counseling","Pharmacology","Hospital Pharmacy","EMR"],
        "Drug Regulatory Affairs":  ["Regulatory","CTD Dossier","FDA/CDSCO","GMP","Drug Laws","Documentation"],
        "Quality Assurance Manager":["GMP","GLP","SOP","Validation","QMS","Audit"],
        "Pharmaceutical Analyst":   ["HPLC","GC","Spectroscopy","Analytical Chemistry","GLP","Lab Skills"],
        "Pharmacovigilance Officer":["Drug Safety","Adverse Event Reporting","MedDRA","Regulatory","Clinical","E2B"],
    },
    "Drug Technology": {
        "Formulation Scientist":    ["Drug Formulation","Lab Skills","Stability Testing","GMP","HPLC","Research"],
        "Production Pharmacist":    ["Manufacturing","GMP","Validation","Process","Documentation","Quality Control"],
        "Quality Control Analyst":  ["HPLC","GC","SOP","GMP","Lab Skills","Documentation"],
        "Regulatory Affairs Officer":["Regulatory","CTD","GMP","FDA","Drug Laws","Documentation"],
    },
    "Pharmaceutics": {
        "Formulation Scientist":    ["Drug Formulation","Lab Skills","Stability Testing","GMP","HPLC","Research"],
        "Pharmaceutical Researcher":["Drug Discovery","Lab Skills","HPLC","Pharmacology","Research","Publications"],
        "Quality Assurance Manager":["GMP","GLP","SOP","Validation","QMS","Audit"],
        "Pharmaceutical Analyst":   ["HPLC","GC","Spectroscopy","Analytical Chemistry","GLP","Lab Skills"],
    },
    "Pharmacology": {
        "Pharmacologist":           ["Drug Research","Lab Skills","Pharmacokinetics","Animal Studies","Clinical","Publications"],
        "Clinical Research Associate":["GCP","Clinical Trials","Regulatory","Data Management","Protocol","SAS"],
        "Pharmacovigilance Officer":["Drug Safety","Adverse Event Reporting","MedDRA","Regulatory","Clinical","E2B"],
        "Medical Writer":           ["Scientific Writing","Regulatory","MS Word","Research","Communication","Publications"],
    },

    # ── MEDICAL ──────────────────────────────────────────────
    "Medicine & Surgery": {
        "General Physician":        ["Clinical Skills","Diagnosis","Patient Care","Medical Knowledge","EMR","Ethics"],
        "Surgeon":                  ["Surgical Skills","Anatomy","Clinical Skills","Patient Care","Leadership","Research"],
        "Medical Researcher":       ["Research","Statistics","Lab Skills","Publications","Grant Writing","Ethics"],
        "Public Health Doctor":     ["Epidemiology","Public Health","Policy","Statistics","Community Medicine","Research"],
        "Healthcare Administrator": ["Healthcare Management","Policy","Communication","Budget","Leadership","Quality"],
        "Medical Officer":          ["Clinical Skills","Administration","Public Health","Government Schemes","EMR","Ethics"],
    },
    "General Medicine": {
        "Physician / Internist":    ["Internal Medicine","Clinical Skills","Diagnosis","EMR","Patient Care","Ethics"],
        "Medical Researcher":       ["Research","Statistics","Publications","Lab Skills","Grant Writing","Ethics"],
        "Healthcare Administrator": ["Healthcare Management","Policy","Communication","Budget","Leadership","Quality"],
    },
    "Pediatrics": {
        "Pediatrician":             ["Child Health","Clinical Skills","Vaccines","Nutrition","Patient Care","EMR"],
        "Neonatologist":            ["NICU","Neonatal Care","Clinical Skills","Emergency","Research","Ethics"],
    },
    "Dental Surgery": {
        "Dentist":                  ["Clinical Dentistry","Dental Surgery","Patient Care","Radiology","Prosthodontics","Ethics"],
        "Orthodontist":             ["Orthodontics","Braces","Clinical Skills","X-Ray","Patient Care","Research"],
        "Dental Researcher":        ["Research","Publications","Lab Skills","Clinical Trials","Statistics","Ethics"],
        "Dental College Faculty":   ["Teaching","Research","Clinical Skills","Publications","Leadership","Ethics"],
    },

    # ── LAW ──────────────────────────────────────────────────
    "Law": {
        "Corporate Lawyer":         ["Contract Law","M&A","Company Law","Legal Research","Drafting","Negotiation"],
        "Criminal Lawyer":          ["Criminal Law","Court Practice","Evidence","Legal Research","Advocacy","IPC"],
        "Civil Lawyer":             ["CPC","Property Law","Family Law","Legal Research","Drafting","Advocacy"],
        "Legal Advisor":            ["Legal Research","Compliance","Risk","Contract","Communication","Drafting"],
        "Judge / Magistrate":       ["Legal Knowledge","Judgment Writing","IPC","CPC","Ethics","Research"],
        "Legal Analyst":            ["Legal Research","Data Analysis","Excel","Policy","Writing","Compliance"],
        "Public Prosecutor":        ["Criminal Law","IPC","CrPC","Evidence","Court Practice","Advocacy"],
        "Human Rights Lawyer":      ["Human Rights Law","Constitutional Law","Advocacy","NGO","Legal Research","Policy"],
    },
    "Corporate Law": {
        "Corporate Lawyer":         ["Contract Law","M&A","Company Law","Legal Research","Drafting","Negotiation"],
        "Legal Advisor":            ["Legal Research","Compliance","Risk","Contract","Communication","Drafting"],
        "Compliance Officer":       ["Regulatory Compliance","SEBI","Company Law","Risk","Audit","Reporting"],
        "Investment Banking Analyst":["Financial Modeling","M&A","Due Diligence","Valuation","Excel","Legal"],
    },
    "Criminal Law": {
        "Criminal Lawyer":          ["Criminal Law","Court Practice","Evidence","Legal Research","Advocacy","IPC"],
        "Public Prosecutor":        ["Criminal Law","IPC","CrPC","Evidence","Court Practice","Advocacy"],
        "Legal Aid Lawyer":         ["Criminal Law","Legal Research","Advocacy","Ethics","Communication","Court"],
    },
    "Constitutional Law": {
        "Constitutional Lawyer":    ["Constitutional Law","Supreme Court Practice","PIL","Legal Research","Advocacy","Policy"],
        "Legal Academic":           ["Research","Teaching","Publications","Constitutional Law","Policy","Writing"],
    },

    # ── ARCHITECTURE ─────────────────────────────────────────
    "Architecture": {
        "Architect":                ["AutoCAD","Revit","SketchUp","Design","Construction","3ds Max"],
        "Interior Designer":        ["AutoCAD","3ds Max","V-Ray","Space Planning","Material Selection","Revit"],
        "Urban Designer":           ["AutoCAD","GIS","Urban Planning","SketchUp","Rhino","Design"],
        "Landscape Architect":      ["AutoCAD","SketchUp","Planting Design","GIS","3ds Max","Sustainability"],
        "BIM Manager":              ["Revit","BIM","Navisworks","AutoCAD","Coordination","Construction"],
        "Construction Project Manager":["MS Project","Construction Mgmt","Contract","AutoCAD","Cost Control","BIM"],
        "Sustainable Architect":    ["Green Building","LEED","Energy Modeling","AutoCAD","Revit","Sustainability"],
    },
    "Interior Design": {
        "Interior Designer":        ["AutoCAD","3ds Max","V-Ray","Space Planning","Material Selection","Revit"],
        "Visual Merchandiser":      ["Display Design","Retail Design","AutoCAD","Creativity","Color Theory","Photoshop"],
        "Set Designer":             ["Set Design","AutoCAD","3ds Max","Creativity","Props","Communication"],
    },
    "Urban Planning": {
        "Urban Planner":            ["GIS","AutoCAD","Urban Design","Zoning","Policy","Statistics"],
        "Transportation Planner":   ["GIS","Traffic Analysis","AutoCAD","Urban Planning","Policy","VISSIM"],
        "Smart City Consultant":    ["GIS","IoT","Data Analytics","Policy","Urban Planning","Smart Solutions"],
    },

    # ── BSC ──────────────────────────────────────────────────
    "Computer Science (BSc)": {
        "Software Developer":       ["Java","Python","JavaScript","React","SQL","Git"],
        "Data Analyst":             ["Python","SQL","Excel","Statistics","Tableau","Power BI"],
        "System Analyst":           ["System Design","SQL","Project Management","Communication","Analysis","Documentation"],
        "Web Developer":            ["HTML","CSS","JavaScript","React","PHP","MySQL"],
        "Cybersecurity Analyst":    ["Networking","Linux","Python","Ethical Hacking","Firewalls","SIEM"],
    },
    "Mathematics": {
        "Data Scientist":           ["Python","R","Statistics","Machine Learning","SQL","Visualization"],
        "Statistician":             ["SPSS","R","SAS","Statistics","Survey Design","Data Analysis"],
        "Actuary":                  ["Actuarial Science","Statistics","Excel","Risk","Insurance","Mathematics"],
        "Operations Research Analyst":["Linear Programming","Python","R","Optimization","Statistics","Excel"],
        "Financial Analyst":        ["Excel","Financial Modeling","Statistics","Bloomberg","Mathematics","CFA"],
        "Teacher / Lecturer":       ["Teaching","Mathematics","Communication","Curriculum","Research","Patience"],
    },
    "Physics": {
        "Research Scientist":       ["Research","Lab Skills","MATLAB","Physics","Publications","Mathematics"],
        "Data Scientist":           ["Python","Statistics","Machine Learning","Mathematics","SQL","Research"],
        "Defense Scientist":        ["Physics","Research","Defense Systems","Mathematics","Lab Skills","Clearance"],
        "Nuclear Engineer":         ["Nuclear Physics","Radiation","Safety","MATLAB","Research","Lab Skills"],
        "Teacher / Lecturer":       ["Teaching","Physics","Communication","Curriculum","Research","Laboratory"],
    },
    "Chemistry": {
        "Analytical Chemist":       ["HPLC","GC","Spectroscopy","Lab Skills","GLP","Documentation"],
        "Research Scientist":       ["Research","Lab Skills","Publications","Chemical Analysis","HPLC","GC-MS"],
        "Quality Control Chemist":  ["HPLC","GC","SOP","GMP","Lab Skills","Documentation"],
        "Pharmaceutical Chemist":   ["Drug Synthesis","Lab Skills","HPLC","GMP","Research","Pharmacology"],
        "Environmental Chemist":    ["Environmental Analysis","Lab Skills","GIS","EIA","Water Testing","Reporting"],
        "Teacher / Lecturer":       ["Teaching","Chemistry","Communication","Lab","Curriculum","Research"],
    },
    "Biology": {
        "Biologist / Researcher":   ["Lab Skills","Research","PCR","Microscopy","Publications","Data Analysis"],
        "Microbiologist":           ["Microbiology","Lab Skills","PCR","Cell Culture","Sterilization","Research"],
        "Environmental Scientist":  ["Field Research","Lab Skills","GIS","Data Analysis","EIA","Report Writing"],
        "Wildlife Biologist":       ["Field Research","Species Identification","GIS","Data Collection","Conservation","Report Writing"],
        "Teacher / Lecturer":       ["Teaching","Biology","Communication","Lab","Curriculum","Research"],
    },
    "Biotechnology (BSc)": {
        "Biotech Lab Technician":   ["PCR","Cell Culture","ELISA","Lab Skills","Data Recording","Safety"],
        "Bioinformatics Analyst":   ["Python","R","BLAST","Bioinformatics","Genomics","Linux"],
        "Quality Control Analyst":  ["HPLC","GC","SOP","GMP","Lab Skills","Documentation"],
        "Research Assistant":       ["Lab Skills","Research","Data Analysis","PCR","Microscopy","Documentation"],
        "Pharmaceutical Sales Rep": ["Product Knowledge","Sales","Communication","Pharmacology","CRM","Marketing"],
    },
    "Nursing": {
        "Clinical Nurse":           ["Patient Care","Clinical Skills","EMR","BLS","ACLS","Documentation"],
        "ICU Nurse":                ["Critical Care","Ventilator","Patient Monitoring","ACLS","BLS","EMR"],
        "Community Health Nurse":   ["Community Health","Health Education","Public Health","Immunization","First Aid","Counseling"],
        "Nurse Manager":            ["Leadership","Healthcare Management","Staff Training","Quality","Budget","Communication"],
        "Healthcare Educator":      ["Teaching","Nursing","Communication","Curriculum","Clinical Skills","Research"],
        "Midwife":                  ["Obstetrics","Maternal Care","Delivery Skills","Patient Care","Neonatal Care","BLS"],
    },
    "Microbiology": {
        "Microbiologist":           ["Microbiology","Lab Skills","PCR","Cell Culture","Sterilization","Research"],
        "Clinical Lab Technician":  ["Lab Skills","Microscopy","PCR","Blood Analysis","Sterilization","Documentation"],
        "Quality Control Analyst":  ["GMP","SOP","Lab Skills","Documentation","HPLC","Microbiology"],
        "Research Scientist":       ["Research","Lab Skills","Publications","Microbiology","PCR","Data Analysis"],
        "Food Safety Officer":      ["HACCP","Food Safety","Microbiology","Lab Skills","Inspection","GMP"],
    },
    "Agriculture": {
        "Agricultural Scientist":   ["Agronomy","Soil Science","Research","Lab Skills","Data Analysis","Field Work"],
        "Agronomist":               ["Crop Management","Soil Testing","Agronomy","Field Research","Data","Extension"],
        "Agricultural Officer":     ["Agriculture","Government Schemes","Field Work","Data Collection","Extension","Reporting"],
        "Food Technologist":        ["Food Processing","HACCP","Lab Skills","Quality","GMP","Packaging"],
        "Farm Manager":             ["Farm Management","Agronomy","Business","Leadership","Equipment","Irrigation"],
    },

    # ── BA ───────────────────────────────────────────────────
    "Economics": {
        "Economist":                ["Statistics","R","Econometrics","STATA","Research","Policy Analysis"],
        "Financial Analyst":        ["Excel","Financial Modeling","Bloomberg","Statistics","Valuation","CFA"],
        "Policy Analyst":           ["Research","Statistics","Policy Writing","STATA","Economics","Communication"],
        "Data Analyst":             ["SQL","Excel","Power BI","Statistics","Python","Tableau"],
        "Market Research Analyst":  ["SPSS","Survey Design","Statistics","Excel","Report Writing","Communication"],
        "Investment Banker":        ["Financial Modeling","Excel","Valuation","Bloomberg","Communication","CFA"],
        "Economic Journalist":      ["Writing","Research","Economics","Communication","Journalism","Data"],
    },
    "Psychology": {
        "Clinical Psychologist":    ["CBT","Assessment","Counseling","DSM","Ethics","Research"],
        "Counselor / Therapist":    ["Counseling","CBT","Active Listening","Ethics","Case Management","Assessment"],
        "HR Manager":               ["Recruitment","HRIS","Labor Law","Communication","Performance Mgmt","Training"],
        "UX Researcher":            ["User Research","Usability Testing","Figma","Survey Design","Analysis","Communication"],
        "School Counselor":         ["Counseling","Child Psychology","Career Guidance","Communication","Assessment","Ethics"],
        "Organizational Psychologist":["OD","Training","Assessment","Statistics","Leadership","Change Mgmt"],
        "Market Research Analyst":  ["Survey Design","Statistics","SPSS","Consumer Behavior","Research","Communication"],
    },
    "Sociology": {
        "Social Worker":            ["Counseling","Community Work","NGO","Policy","Communication","Research"],
        "NGO Program Manager":      ["Project Management","NGO","Communication","Fundraising","Policy","Research"],
        "Policy Analyst":           ["Research","Policy Writing","Statistics","Communication","Analysis","Advocacy"],
        "HR Specialist":            ["Recruitment","Communication","Labor Law","Training","HRIS","Organizational Behavior"],
        "Journalist / Writer":      ["Writing","Research","Communication","Interviewing","Social Issues","Media"],
        "Research Analyst":         ["Research","Statistics","SPSS","Policy","Communication","Report Writing"],
    },
    "Journalism & Mass Communication": {
        "Journalist / Reporter":    ["Writing","Research","Communication","Interviewing","Media","Digital Tools"],
        "Content Writer":           ["Writing","SEO","Research","Social Media","Content Strategy","Editing"],
        "PR Manager":               ["Public Relations","Communication","Media Relations","Crisis Mgmt","Writing","Social Media"],
        "Digital Marketer":         ["SEO","Social Media","Content Marketing","Analytics","Google Ads","Communication"],
        "Video Producer":           ["Videography","Editing","Adobe Premiere","Scripting","Communication","Storytelling"],
        "Social Media Manager":     ["Social Media","Content Creation","Analytics","Communication","Scheduling","Marketing"],
        "Copy Writer":              ["Writing","Creativity","Marketing","Communication","Research","Brand Voice"],
    },
    "Political Science": {
        "Civil Servant (IAS/IPS)":  ["UPSC Prep","General Knowledge","Essay Writing","Ethics","Indian Polity","Leadership"],
        "Policy Analyst":           ["Research","Policy Writing","Statistics","Communication","Analysis","Political Science"],
        "Political Journalist":     ["Writing","Research","Political Knowledge","Communication","Journalism","Media"],
        "Legal Professional":       ["Legal Research","Political Science","Law","Advocacy","Communication","Writing"],
        "International Relations":  ["Diplomacy","International Law","Research","Languages","Communication","Global Affairs"],
        "NGO Leader":               ["Leadership","Communication","Fundraising","Policy","Community Work","Research"],
    },
    "English Literature": {
        "Content Writer":           ["Writing","SEO","Research","Editing","Creativity","Communication"],
        "Editor":                   ["Editing","Writing","Grammar","Publishing","Communication","Research"],
        "Teacher / Lecturer":       ["Teaching","English","Communication","Curriculum","Research","Patience"],
        "Journalist":               ["Writing","Research","Communication","Interviewing","Media","Editing"],
        "Copy Writer":              ["Writing","Creativity","Marketing","Communication","Brand Voice","Research"],
        "Technical Writer":         ["Technical Writing","Documentation","Research","MS Word","Communication","Editing"],
    },
    "Social Work": {
        "Social Worker":            ["Counseling","Community Work","NGO","Policy","Communication","Research"],
        "NGO Program Manager":      ["Project Management","NGO","Communication","Fundraising","Policy","Research"],
        "Child Welfare Officer":    ["Child Protection","Counseling","Case Management","Communication","Policy","Ethics"],
        "Community Development Officer":["Community Work","NGO","Leadership","Communication","Field Work","Policy"],
        "Hospital Social Worker":   ["Medical Social Work","Counseling","Patient Support","Communication","Healthcare","Ethics"],
    },

    # ── BCA / MCA ────────────────────────────────────────────
    "Computer Applications": {
        "Software Developer":       ["Java","Python","JavaScript","React","SQL","Git"],
        "Web Developer":            ["HTML","CSS","JavaScript","React","PHP","MySQL"],
        "Mobile App Developer":     ["Android","iOS","React Native","Flutter","Java","Kotlin"],
        "Database Administrator":   ["Oracle","MySQL","SQL Server","SQL","Backup","Performance Tuning"],
        "System Analyst":           ["System Design","SQL","Project Management","Communication","Analysis","Documentation"],
        "IT Support Engineer":      ["Networking","Windows","Linux","Hardware","Troubleshooting","Communication"],
        "Quality Assurance Tester": ["Selenium","Manual Testing","JIRA","Python","Automation","API Testing"],
    },
    "Cloud Computing": {
        "Cloud Engineer":           ["AWS","Azure","GCP","Terraform","Docker","Linux"],
        "DevOps Engineer":          ["Docker","Kubernetes","CI/CD","Linux","AWS","Jenkins"],
        "Cloud Architect":          ["AWS","Azure","Cloud Design","Terraform","Security","Networking"],
        "Site Reliability Engineer":["Linux","Python","Kubernetes","Monitoring","AWS","Automation"],
    },
    "Cybersecurity": {
        "Cybersecurity Analyst":    ["Networking","Linux","Python","Ethical Hacking","Firewalls","SIEM"],
        "Penetration Tester":       ["Kali Linux","Metasploit","Python","Network Security","OWASP","CEH"],
        "Security Architect":       ["Security Design","Firewalls","Cloud Security","Risk","Compliance","Networking"],
        "Incident Response Analyst":["SIEM","Forensics","Linux","Python","Threat Analysis","Incident Response"],
    },

    # ── BCOM / BBA ───────────────────────────────────────────
    "Commerce": {
        "Chartered Accountant":     ["Accounting","Taxation","Tally","Excel","Audit","GST"],
        "Financial Analyst":        ["Excel","Financial Modeling","Accounting","Bloomberg","Valuation","CFA"],
        "Tax Consultant":           ["Taxation","GST","Income Tax","Tally","Excel","Compliance"],
        "Auditor":                  ["Audit","Accounting","Excel","Risk","Internal Controls","IFRS"],
        "Cost Accountant (CMA)":    ["CMA","Costing","Excel","ERP","Budgeting","SAP"],
        "Banking Professional":     ["Banking","Finance","Excel","Customer Service","Compliance","Risk"],
        "E-commerce Manager":       ["E-commerce","Digital Marketing","Excel","Analytics","Operations","Supply Chain"],
    },
    "Accounting & Finance": {
        "Chartered Accountant":     ["Accounting","Taxation","Tally","Excel","Audit","GST"],
        "Financial Analyst":        ["Excel","Financial Modeling","Accounting","Bloomberg","Valuation","CFA"],
        "Investment Analyst":       ["Financial Modeling","Excel","Bloomberg","Valuation","Research","CFA"],
        "Tax Consultant":           ["Taxation","GST","Income Tax","Tally","Excel","Compliance"],
        "Auditor":                  ["Audit","Accounting","Excel","Risk","Internal Controls","IFRS"],
    },
    "Banking & Insurance": {
        "Bank Manager":             ["Banking Operations","Finance","Leadership","Customer Service","Risk","Compliance"],
        "Insurance Underwriter":    ["Risk Assessment","Insurance","Excel","Actuarial","Communication","Finance"],
        "Credit Analyst":           ["Credit Risk","Excel","Financial Analysis","Banking","Communication","Finance"],
        "Relationship Manager":     ["Customer Relations","Banking","Finance","Communication","Sales","CRM"],
        "Actuary":                  ["Actuarial Science","Statistics","Excel","Risk","Insurance","Mathematics"],
    },
    "Business Administration": {
        "Business Development Manager":["Sales","Communication","Market Research","CRM","Negotiation","Strategy"],
        "Operations Manager":       ["Operations","Supply Chain","Excel","Process Improvement","Leadership","ERP"],
        "Marketing Manager":        ["Digital Marketing","SEO","Analytics","Content Strategy","CRM","Social Media"],
        "HR Manager":               ["Recruitment","HRIS","Labor Law","Training","Performance","Compensation"],
        "Entrepreneur":             ["Business Planning","Finance","Marketing","Leadership","Networking","Strategy"],
        "Management Consultant":    ["Strategy","Problem Solving","Excel","PPT","Communication","Analytics"],
        "Product Manager":          ["Product Strategy","Agile","User Research","SQL","Data Analysis","Roadmapping"],
    },
    "Marketing": {
        "Digital Marketer":         ["SEO","Google Ads","Social Media","Analytics","Content Marketing","Email Marketing"],
        "Brand Manager":            ["Brand Strategy","Marketing","Communication","Analytics","Consumer Research","Creativity"],
        "Market Research Analyst":  ["SPSS","Survey Design","Statistics","Excel","Report Writing","Consumer Insights"],
        "Sales Manager":            ["Sales","CRM","Negotiation","Communication","Target Achievement","Leadership"],
        "Social Media Manager":     ["Social Media","Content Creation","Analytics","Communication","Scheduling","Marketing"],
        "Content Marketer":         ["Content Strategy","SEO","Writing","Analytics","Social Media","Creativity"],
    },
    "Human Resources": {
        "HR Manager":               ["Recruitment","HRIS","Labor Law","Training","Performance","Compensation"],
        "Talent Acquisition Specialist":["Recruitment","LinkedIn","ATS","Communication","HR","Negotiation"],
        "Learning & Development Manager":["Training","L&D","LMS","Communication","Curriculum Design","Leadership"],
        "HR Business Partner":      ["HR Strategy","Communication","Employee Relations","Data Analytics","Leadership","Change Mgmt"],
        "Payroll Manager":          ["Payroll","Excel","HRIS","Tax","Compliance","Accounting"],
        "Employee Relations Specialist":["Labor Law","Communication","Conflict Resolution","HR Policy","Ethics","Counseling"],
    },
    "Finance": {
        "Financial Analyst":        ["Excel","Financial Modeling","Bloomberg","Valuation","Research","CFA"],
        "Investment Banker":        ["Financial Modeling","Excel","Valuation","M&A","Bloomberg","Communication"],
        "Portfolio Manager":        ["Investment","CFA","Bloomberg","Excel","Risk","Portfolio Theory"],
        "Risk Manager":             ["Risk Management","Basel","Excel","Financial Modeling","Compliance","Statistics"],
        "Financial Planner":        ["CFP","Financial Planning","Excel","Tax","Insurance","Client Management"],
    },

    # ── MBA ───────────────────────────────────────────────────
    "General Management": {
        "General Manager":          ["Leadership","Strategy","Finance","Operations","Communication","P&L Management"],
        "Management Consultant":    ["Strategy","Problem Solving","Excel","PPT","Communication","Analytics"],
        "Business Development Manager":["Sales","Communication","Market Research","CRM","Negotiation","Strategy"],
        "Entrepreneur":             ["Business Planning","Finance","Marketing","Leadership","Networking","Strategy"],
        "CEO / Managing Director":  ["Leadership","Strategy","Finance","Vision","Communication","Decision Making"],
    },
    "Business Analytics": {
        "Business Analyst":         ["SQL","Excel","Power BI","Requirements","Process Mapping","Agile"],
        "Data Analyst":             ["SQL","Python","Tableau","Statistics","Excel","Communication"],
        "Strategy Analyst":         ["Excel","PPT","Strategy","Research","Analytics","Communication"],
        "Product Analyst":          ["SQL","Product Analytics","Python","A/B Testing","User Research","Excel"],
        "Operations Analyst":       ["Excel","SQL","Process Improvement","Supply Chain","Lean","Analytics"],
    },
    "Healthcare Management": {
        "Hospital Administrator":   ["Healthcare Management","Policy","Communication","Budget","Leadership","Quality"],
        "Healthcare Consultant":    ["Healthcare Strategy","Analytics","Communication","Policy","Process Improvement","Excel"],
        "Health Insurance Manager": ["Insurance","Healthcare","Compliance","Risk","Communication","Finance"],
        "Public Health Manager":    ["Public Health","Epidemiology","Policy","Budget","Communication","Research"],
    },

    # ── HOTEL MANAGEMENT ─────────────────────────────────────
    "Hotel Management": {
        "Hotel Manager":            ["Hospitality","Operations","Leadership","Customer Service","Revenue Mgmt","Communication"],
        "F&B Manager":              ["Food & Beverage","Operations","Leadership","Menu Planning","Cost Control","Communication"],
        "Front Office Manager":     ["Guest Relations","PMS Software","Communication","Leadership","Revenue Mgmt","Hospitality"],
        "Event Manager":            ["Event Planning","Communication","Budgeting","Vendor Management","Creativity","Leadership"],
        "Revenue Manager":          ["Revenue Management","Excel","Analytics","Pricing","Hospitality","OTA Management"],
        "Housekeeping Manager":     ["Housekeeping Operations","Leadership","Quality Control","Budget","Communication","Hospitality"],
    },
    "Culinary Arts": {
        "Chef":                     ["Culinary Skills","Kitchen Management","Menu Planning","Food Safety","Creativity","Leadership"],
        "Pastry Chef":              ["Baking","Pastry","Creativity","Food Safety","Menu Design","Kitchen Mgmt"],
        "Food Stylist":             ["Food Photography","Styling","Creativity","Photoshop","Communication","Culinary Skills"],
        "Restaurant Manager":       ["Restaurant Operations","Customer Service","Leadership","Finance","Communication","F&B"],
    },

    # ── FINE ARTS / BFA ──────────────────────────────────────
    "Fine Arts": {
        "Graphic Designer":         ["Photoshop","Illustrator","InDesign","Creativity","Typography","Brand Design"],
        "UI/UX Designer":           ["Figma","Adobe XD","User Research","Prototyping","Creativity","Wireframing"],
        "Animation Artist":         ["Maya","Blender","After Effects","Animation","3D Modeling","Creativity"],
        "Art Director":             ["Creative Direction","Photoshop","Illustrator","Brand","Communication","Leadership"],
        "Illustrator":              ["Illustration","Photoshop","Procreate","Drawing","Creativity","Digital Art"],
        "Art Teacher":              ["Teaching","Fine Arts","Communication","Curriculum","Creativity","Patience"],
    },

    # ── EDUCATION ────────────────────────────────────────────
    "Education": {
        "School Teacher":           ["Teaching","Curriculum","Communication","Subject Knowledge","Classroom Mgmt","Patience"],
        "School Principal":         ["Leadership","Education Management","Communication","Policy","Budget","Staff Mgmt"],
        "Curriculum Designer":      ["Curriculum Design","Education","Research","Communication","Content Creation","Assessment"],
        "Education Consultant":     ["Education Policy","Research","Communication","Training","Analytics","Curriculum"],
        "Special Education Teacher":["Special Education","Patience","IEP","Communication","Psychology","Counseling"],
        "Corporate Trainer":        ["Training","Communication","L&D","Curriculum","Facilitation","Leadership"],
    },
}

# ── Flatten for easy lookup ──────────────────────────────────
def get_careers_for_course(degree, branch):
    # Direct match
    if branch in CAREER_DATA:
        return CAREER_DATA[branch]
    # Match with degree suffix e.g. "Computer Science" from BSc
    for key in CAREER_DATA:
        if branch.lower() == key.lower():
            return CAREER_DATA[key]
        if branch.lower() in key.lower() or key.lower() in branch.lower():
            return CAREER_DATA[key]
    # Degree-based fallbacks
    fallbacks = {
        "MBA": CAREER_DATA["General Management"],
        "BBA": CAREER_DATA["Business Administration"],
        "LLB": CAREER_DATA["Law"],
        "LLM": CAREER_DATA["Constitutional Law"],
        "BArch": CAREER_DATA["Architecture"],
        "MArch": CAREER_DATA["Architecture"],
        "BPharma": CAREER_DATA["Pharmacy"],
        "MPharma": CAREER_DATA["Pharmaceutics"],
        "MBBS": CAREER_DATA["Medicine & Surgery"],
        "MD": CAREER_DATA["General Medicine"],
        "BDS": CAREER_DATA["Dental Surgery"],
        "BEd": CAREER_DATA["Education"],
        "MEd": CAREER_DATA["Education"],
        "BFA": CAREER_DATA["Fine Arts"],
        "BHM": CAREER_DATA["Hotel Management"],
        "BCA": CAREER_DATA["Computer Applications"],
        "MCA": CAREER_DATA["Computer Applications"],
    }
    if degree in fallbacks:
        return fallbacks[degree]
    return {
        "Software Developer":   ["Programming","Problem Solving","Algorithms","Communication","Teamwork","Git"],
        "Data Analyst":         ["SQL","Excel","Statistics","Communication","Python","Visualization"],
        "Business Analyst":     ["Excel","Communication","Requirements","Process Mapping","SQL","Presentation"],
        "Researcher":           ["Research","Writing","Statistics","Critical Thinking","Domain Knowledge","Ethics"],
        "Consultant":           ["Communication","Problem Solving","Excel","Presentation","Domain Knowledge","Analysis"],
        "Entrepreneur":         ["Business Planning","Communication","Leadership","Marketing","Finance","Networking"],
    }

def predict_career(skills, cgpa, degree="BTech", branch="Computer Science"):
    careers = get_careers_for_course(degree, branch)
    skills_lower = [s.strip().lower() for s in skills if s.strip()]
    results = []
    for career, required in careers.items():
        req_lower = [r.lower() for r in required]
        matched = sum(1 for s in skills_lower if s in req_lower)
        base = (matched / len(required) * 100) if required else 0
        bonus = min((cgpa - 6.0) * 2, 5) if cgpa >= 6.0 else 0
        score = min(round(base + bonus, 1), 99)
        results.append({"name":career,"score":score,"matched":matched,"total":len(required),"icon":_icon(career)})
    results.sort(key=lambda x: x["score"], reverse=True)
    return results

def get_skill_gap(my_skills, target, degree="BTech", branch="Computer Science"):
    careers = get_careers_for_course(degree, branch)
    if target not in careers:
        target = list(careers.keys())[0]
    required = careers.get(target, [])
    my_lower = [s.strip().lower() for s in my_skills if s.strip()]
    have    = [s for s in required if s.lower() in my_lower]
    missing = [s for s in required if s.lower() not in my_lower]
    pct = round(len(have)/len(required)*100) if required else 0
    return {"target":target,"have":have,"missing":missing,"percent":pct}

ROADMAPS = {
    "AI Engineer":          [{"month":"Month 1","title":"Python & DSA","topics":["Python OOP","Algorithms","Data Structures","Git","Linux"]},{"month":"Month 2","title":"Machine Learning","topics":["Regression","Classification","Clustering","Scikit-Learn","Model Eval"]},{"month":"Month 3","title":"Deep Learning","topics":["Neural Networks","CNNs","RNNs","TensorFlow","PyTorch"]},{"month":"Month 4","title":"Projects","topics":["2 End-to-End ML Projects","Kaggle","GitHub Portfolio","Documentation"]},{"month":"Month 5","title":"MLOps & Cloud","topics":["Docker","MLflow","AWS","FastAPI","Deployment"]},{"month":"Month 6","title":"Job Ready","topics":["Resume","LinkedIn","Mock Interviews","Apply to Jobs"]}],
    "Software Developer":   [{"month":"Month 1","title":"Core Programming","topics":["Java/Python","OOP","Data Structures","Algorithms","Git"]},{"month":"Month 2","title":"Web Development","topics":["HTML","CSS","JavaScript","React","Node.js"]},{"month":"Month 3","title":"Backend & Database","topics":["REST APIs","SQL","MongoDB","Docker","Authentication"]},{"month":"Month 4","title":"Full Stack Project","topics":["Build Project","GitHub","Code Review","Testing","Documentation"]},{"month":"Month 5","title":"Cloud & DevOps","topics":["AWS","CI/CD","Linux","Docker","Deployment"]},{"month":"Month 6","title":"Job Ready","topics":["Resume","DSA Practice","Mock Interviews","Applications"]}],
    "Clinical Pharmacist":  [{"month":"Month 1","title":"Pharmacology Deep Dive","topics":["Drug Classes","Pharmacokinetics","Adverse Effects","Drug Interactions","Therapeutics"]},{"month":"Month 2","title":"Hospital Pharmacy","topics":["Ward Rounds","Drug Dispensing","Patient Counseling","EMR Systems","Formulary Mgmt"]},{"month":"Month 3","title":"Clinical Skills","topics":["Case Studies","Drug Monitoring","Lab Values","Prescription Review","Clinical Guidelines"]},{"month":"Month 4","title":"Hospital Internship","topics":["Clinical Rotation","Patient Cases","Doctor Collaboration","Documentation","Professional Ethics"]},{"month":"Month 5","title":"Certifications","topics":["Clinical Pharmacy Cert","NABH Standards","Pharmacovigilance","Drug Information"]},{"month":"Month 6","title":"Job Ready","topics":["Resume","Hospital Applications","Interview Prep","Licensing Registration"]}],
    "Corporate Lawyer":     [{"month":"Month 1","title":"Legal Foundations","topics":["Contract Law","Company Law","Legal Research","LexisNexis","Bare Acts"]},{"month":"Month 2","title":"Drafting Skills","topics":["Contract Drafting","MOUs","NDA","Legal Writing","Pleadings"]},{"month":"Month 3","title":"Corporate Law","topics":["M&A","Due Diligence","SEBI Regulations","Compliance","Company Law"]},{"month":"Month 4","title":"Law Firm Internship","topics":["Client Meetings","Research Memos","Court Visits","Professional Ethics","Networking"]},{"month":"Month 5","title":"Specialization","topics":["Tax/IP/Banking Law","Moot Court","Publications","Bar Council"]},{"month":"Month 6","title":"Job Ready","topics":["Resume","Law Firm Applications","Enrollment","Networking"]}],
    "Structural Engineer":  [{"month":"Month 1","title":"Design Software","topics":["AutoCAD","STAAD Pro","ETABS","IS Codes","Drawing Reading"]},{"month":"Month 2","title":"Structural Analysis","topics":["RCC Design","Steel Design","Load Calculations","Foundation","SAP2000"]},{"month":"Month 3","title":"Construction Mgmt","topics":["MS Project","Cost Estimation","Bar Bending","Safety","Specifications"]},{"month":"Month 4","title":"Field Experience","topics":["Site Visit","Lab Testing","Survey","Technical Report","Drawings"]},{"month":"Month 5","title":"Certifications","topics":["AutoCAD Cert","STAAD Pro Advanced","IS Code Study","GATE Prep"]},{"month":"Month 6","title":"Job Ready","topics":["Resume","PSU Applications","GATE Exam","Interviews"]}],
    "Mechanical Design Engineer":[{"month":"Month 1","title":"CAD Tools","topics":["AutoCAD","SolidWorks","CATIA","Drawing Standards","GD&T"]},{"month":"Month 2","title":"Analysis & Simulation","topics":["ANSYS","FEA","MATLAB","Simulation","Meshing"]},{"month":"Month 3","title":"Core Engineering","topics":["Thermodynamics","Fluid Mechanics","Manufacturing","Materials","Quality"]},{"month":"Month 4","title":"Design Projects","topics":["Design Project","Report Writing","Peer Review","Presentations","Industry Visit"]},{"month":"Month 5","title":"Specialization","topics":["Automotive/Robotics/Thermal","Advanced Software","Certifications"]},{"month":"Month 6","title":"Job Ready","topics":["Resume","Core Company Prep","Campus Placements","Interview"]}],
    "Architect":            [{"month":"Month 1","title":"Design Software","topics":["AutoCAD","Revit","SketchUp","Design Principles","Hand Drafting"]},{"month":"Month 2","title":"3D & Rendering","topics":["3ds Max","V-Ray","Lumion","Model Making","Presentation Skills"]},{"month":"Month 3","title":"Construction Knowledge","topics":["Building Materials","Construction Methods","IS Codes","Structural Basics","MEP"]},{"month":"Month 4","title":"Architecture Internship","topics":["Design Office","Client Projects","Site Visits","Working Drawings","Coordination"]},{"month":"Month 5","title":"Specialization","topics":["BIM/Revit Advanced","Sustainable Design","LEED","Urban Design","Portfolio"]},{"month":"Month 6","title":"Council of Architecture","topics":["COA Registration","Resume","Portfolio","Job Applications","Studio Setup"]}],
    "Journalist / Reporter":[{"month":"Month 1","title":"Writing & Research","topics":["News Writing","AP Style","Research Skills","Source Building","Fact Checking"]},{"month":"Month 2","title":"Digital Media","topics":["CMS Tools","SEO","Social Media","Video Basics","Photography"]},{"month":"Month 3","title":"Beat Reporting","topics":["Choose Beat: Politics/Crime/Business","Field Reporting","Interviews","Ethics","Deadlines"]},{"month":"Month 4","title":"Media Internship","topics":["Newspaper/TV/Digital Internship","Breaking News","Editing","Professional Network"]},{"month":"Month 5","title":"Multimedia Skills","topics":["Video Editing","Podcast","Data Journalism","Adobe Premiere","Storytelling"]},{"month":"Month 6","title":"Job Ready","topics":["Portfolio","Resume","Media House Applications","Freelancing","Personal Brand"]}],
    "HR Manager":           [{"month":"Month 1","title":"HR Fundamentals","topics":["Recruitment","Labor Law","HRIS","Compensation","Org Behavior"]},{"month":"Month 2","title":"Talent Management","topics":["JD Writing","Interview Skills","ATS","Onboarding","Employee Engagement"]},{"month":"Month 3","title":"HR Tools","topics":["Excel","SAP HR","Workday","Performance Mgmt","HRMS"]},{"month":"Month 4","title":"HR Internship","topics":["End-to-End Recruitment","Payroll","Policy Drafting","L&D Support","Professional Network"]},{"month":"Month 5","title":"Certifications","topics":["SHRM","PHRi","HR Analytics","Excel Advanced","Labor Law Cert"]},{"month":"Month 6","title":"Job Ready","topics":["Resume","LinkedIn","HR Job Applications","Interview Prep","Mock HR Rounds"]}],
    "Financial Analyst":    [{"month":"Month 1","title":"Finance Fundamentals","topics":["Accounting","Financial Statements","Excel","Valuation","Economics"]},{"month":"Month 2","title":"Financial Modeling","topics":["DCF","LBO","Comparable Analysis","Excel Advanced","Bloomberg"]},{"month":"Month 3","title":"Investment Analysis","topics":["Equity Research","Sector Analysis","Financial News","Ratios","Research Reports"]},{"month":"Month 4","title":"Finance Internship","topics":["Investment Bank/Firm Internship","Client Reports","Market Research","Excel Models","Professional Network"]},{"month":"Month 5","title":"Certifications","topics":["CFA Level 1","FRM","Bloomberg Cert","Financial Modeling Cert","Excel VBA"]},{"month":"Month 6","title":"Job Ready","topics":["Resume","LinkedIn","Finance Job Applications","Interview Prep","Technical Mock"]}],
    "Digital Marketer":     [{"month":"Month 1","title":"Marketing Foundations","topics":["Marketing Principles","Consumer Behavior","Brand Building","Market Research","Excel"]},{"month":"Month 2","title":"Digital Tools","topics":["Google Ads","SEO","Social Media Marketing","Email Marketing","Analytics"]},{"month":"Month 3","title":"Content & Social Media","topics":["Content Strategy","Instagram/LinkedIn","Video Marketing","Canva","Copywriting"]},{"month":"Month 4","title":"Marketing Internship","topics":["Campaign Management","Client Projects","Performance Reporting","A/B Testing","Brand Projects"]},{"month":"Month 5","title":"Certifications","topics":["Google Ads Cert","HubSpot","Meta Blueprint","SEO Cert","Analytics Cert"]},{"month":"Month 6","title":"Job Ready","topics":["Portfolio","Resume","Agency/Brand Applications","Freelancing","Interview Prep"]}],
    "Chef":                 [{"month":"Month 1","title":"Kitchen Fundamentals","topics":["Knife Skills","Cooking Methods","Food Safety","HACCP","Mise en Place"]},{"month":"Month 2","title":"Cuisine Specialization","topics":["Indian/Continental/Asian Cuisine","Sauces","Stocks","Pastry Basics","Plating"]},{"month":"Month 3","title":"Advanced Cooking","topics":["Menu Planning","Cost Control","Molecular Gastronomy","Advanced Baking","Nutrition"]},{"month":"Month 4","title":"Kitchen Internship","topics":["5-Star Hotel Kitchen","Line Cook Experience","Kitchen Hierarchy","Speed & Accuracy","Hygiene"]},{"month":"Month 5","title":"Specialization","topics":["Choose: Pastry/Italian/Asian","Food Photography","Food Business","Restaurant Management"]},{"month":"Month 6","title":"Career Launch","topics":["Culinary Portfolio","Resume","Hotel/Restaurant Applications","Freelance Catering","Food Blog"]}],
    "Default":              [{"month":"Month 1","title":"Core Subject Mastery","topics":["Strengthen Domain Knowledge","Online Courses","Textbooks","Practice Problems","Study Group"]},{"month":"Month 2","title":"Technical Skills","topics":["Domain-Specific Software","Certifications","Coursera/NPTEL","Skill Building","Tools"]},{"month":"Month 3","title":"Projects","topics":["Mini Project","Case Study","Research Paper","Portfolio Building","Documentation"]},{"month":"Month 4","title":"Internship Preparation","topics":["Resume Building","LinkedIn","Cover Letters","Mock Interviews","Networking"]},{"month":"Month 5","title":"Internship / Training","topics":["Industry Internship","Professional Skills","Networking","Practical Learning","Mentorship"]},{"month":"Month 6","title":"Job Ready","topics":["Final Resume Polish","Company Research","Interview Prep","Applications","Offer Negotiation"]}],
}

def get_roadmap(target):
    for key in ROADMAPS:
        if key == "Default": continue
        if key.lower() == target.lower() or key.lower() in target.lower() or target.lower() in key.lower():
            return ROADMAPS[key]
    return ROADMAPS["Default"]

def _icon(career):
    icons = {
        "AI":"🤖","Data Scientist":"🔬","ML":"⚙️","Data Analyst":"📊","NLP":"💬",
        "Computer Vision":"👁️","Software":"💻","Full Stack":"🌐","Backend":"🔧",
        "DevOps":"🚀","Cyber":"🔒","Cloud":"☁️","Mechanical":"⚙️","Design Engineer":"✏️",
        "Civil":"🏗️","Structural":"🏛️","Corporate Lawyer":"⚖️","Criminal Lawyer":"⚖️",
        "Lawyer":"⚖️","Legal":"⚖️","Doctor":"🏥","Physician":"🏥","Surgeon":"🏥",
        "Nurse":"🏥","Pharmacist":"💊","Pharmaceutical":"💊","Drug":"💊",
        "Architect":"🏛️","Interior":"🏠","Urban":"🌆","Financial":"💰",
        "HR":"👥","Marketing":"📣","Product Manager":"🎯","Researcher":"🔬",
        "Entrepreneur":"🚀","Consultant":"💼","Business":"📈","Chartered":"📒",
        "Journalist":"📰","Writer":"✍️","Content":"✍️","Teacher":"📚","Chef":"👨‍🍳",
        "Hotel":"🏨","Social Worker":"🤝","NGO":"🤝","Economist":"📈",
        "Psychologist":"🧠","Counselor":"🧠","Biologist":"🧬","Biotech":"🧬",
        "Agricultural":"🌾","Environmental":"🌿","Embedded":"🔌","VLSI":"🔌",
        "IoT":"📡","Telecom":"📡","Electrical":"⚡","Automation":"🤖",
        "Graphic":"🎨","Animation":"🎬","Art":"🎨","Fashion":"👗",
        "Event":"🎪","Tourism":"✈️",
    }
    for k, v in icons.items():
        if k.lower() in career.lower():
            return v
    return "🎯"
