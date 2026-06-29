# model.py — Career Prediction & Skill Gap Engine

CAREER_SKILLS = {
    "AI Engineer":              ["Python","TensorFlow","PyTorch","Deep Learning","MLOps","Docker","Kubernetes","NumPy","Pandas","Scikit-Learn"],
    "Data Scientist":           ["Python","Statistics","Pandas","NumPy","Scikit-Learn","SQL","Matplotlib","Jupyter","R","Tableau"],
    "ML Engineer":              ["Python","PyTorch","TensorFlow","Spark","Airflow","Kubernetes","Docker","SQL","NumPy","Git"],
    "Data Analyst":             ["SQL","Power BI","Excel","Tableau","Python","Pandas","Statistics","Data Viz","Google Sheets","Looker"],
    "NLP Engineer":             ["Python","spaCy","HuggingFace","BERT","NLTK","TensorFlow","PyTorch","Linguistics","REST APIs","SQL"],
    "Computer Vision Engineer": ["Python","OpenCV","YOLO","PyTorch","TensorFlow","CUDA","C++","NumPy","Deep Learning","Docker"],
}

ROADMAPS = {
    "AI Engineer": [
        {"month":"Month 1","title":"Python Advanced & DSA",    "topics":["OOP","Algorithms","Data Structures","Git & GitHub","Linux Basics"]},
        {"month":"Month 2","title":"Machine Learning Core",    "topics":["Regression","Classification","Clustering","Model Evaluation","Scikit-Learn"]},
        {"month":"Month 3","title":"Deep Learning",            "topics":["Neural Networks","CNNs","RNNs","TensorFlow","PyTorch"]},
        {"month":"Month 4","title":"Projects & Kaggle",        "topics":["2 End-to-End Projects","Kaggle Competitions","GitHub Portfolio","Documentation"]},
        {"month":"Month 5","title":"MLOps & Cloud",            "topics":["Docker","MLflow","AWS/GCP Basics","Model Deployment","FastAPI"]},
        {"month":"Month 6","title":"Internship & Job Prep",    "topics":["Resume Polish","LinkedIn Optimization","Mock Interviews","Apply to 50+ Jobs"]},
    ],
    "Data Scientist": [
        {"month":"Month 1","title":"Python & Statistics",      "topics":["Python","Probability","Statistics","NumPy","Pandas"]},
        {"month":"Month 2","title":"Data Analysis",            "topics":["EDA","Matplotlib","Seaborn","SQL","Data Cleaning"]},
        {"month":"Month 3","title":"Machine Learning",         "topics":["Scikit-Learn","Feature Engineering","Model Selection","Cross Validation"]},
        {"month":"Month 4","title":"Advanced ML & Projects",   "topics":["XGBoost","Time Series","NLP Basics","3 Projects"]},
        {"month":"Month 5","title":"Visualization & BI",       "topics":["Tableau","Power BI","Storytelling with Data","Dashboards"]},
        {"month":"Month 6","title":"Job Ready",                "topics":["Portfolio","Resume","Case Study Prep","Interviews"]},
    ],
    "Data Analyst": [
        {"month":"Month 1","title":"SQL Mastery",              "topics":["Basic SQL","Joins","Subqueries","Window Functions","Practice"]},
        {"month":"Month 2","title":"Excel & Power BI",         "topics":["Advanced Excel","Pivot Tables","Power BI Desktop","DAX Basics"]},
        {"month":"Month 3","title":"Python for Analysis",      "topics":["Pandas","NumPy","Matplotlib","Seaborn","EDA Projects"]},
        {"month":"Month 4","title":"Statistics",               "topics":["Descriptive Stats","Hypothesis Testing","A/B Testing","Regression"]},
        {"month":"Month 5","title":"Projects & Dashboard",     "topics":["3 Real Datasets","Dashboard Projects","GitHub","Storytelling"]},
        {"month":"Month 6","title":"Job Applications",         "topics":["Resume","LinkedIn","Interview Prep","50+ Applications"]},
    ],
}

DEFAULT_ROADMAP = ROADMAPS["AI Engineer"]


def predict_career(skills: list, cgpa: float = 7.0) -> list:
    """Score each career based on skill overlap + CGPA boost."""
    skills_lower = [s.strip().lower() for s in skills]
    results = []

    for career, required in CAREER_SKILLS.items():
        required_lower = [r.lower() for r in required]
        matched = sum(1 for s in skills_lower if s in required_lower)
        base_score = (matched / len(required)) * 100

        # CGPA bonus (max +5 points)
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


def get_skill_gap(my_skills: list, target: str) -> dict:
    """Return missing skills for a target career."""
    if target not in CAREER_SKILLS:
        target = "AI Engineer"

    my_lower = [s.strip().lower() for s in my_skills]
    required = CAREER_SKILLS[target]
    missing = [s for s in required if s.lower() not in my_lower]
    have    = [s for s in required if s.lower() in my_lower]

    return {
        "target": target,
        "have": have,
        "missing": missing,
        "percent": round(len(have) / len(required) * 100)
    }


def get_roadmap(target: str) -> list:
    return ROADMAPS.get(target, DEFAULT_ROADMAP)


def _icon(career):
    icons = {
        "AI Engineer":"🤖","Data Scientist":"🔬","ML Engineer":"⚙️",
        "Data Analyst":"📊","NLP Engineer":"💬","Computer Vision Engineer":"👁️"
    }
    return icons.get(career,"🎯")