from .skill_extractor import extract_skills

def missing_skills(resume_path,JD):
    skills_present = extract_skills(resume_path)
    skills_required = extract_skills(JD,True)
    skills_missing  = skills_required-skills_present
    return skills_missing
