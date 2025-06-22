import os
import csv
from pyresparser import ResumeParser
from .text_preprocessing import remove_punctuation
def create_skills_set(path):
    try :
        with open(path,'r',encoding='utf-8') as file :
            reader = csv.reader(file)
            for row in reader : 
                lt = [skill.strip().lower() for skill in row if skill.strip()]
            return set(lt)
    except FileNotFoundError:
        raise FileNotFoundError(f"CSV file not found.")

# For accessing the skills CSV file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
skill_csv = os.path.join(BASE_DIR,'..', 'data', 'skills.csv')
skill_set = create_skills_set(skill_csv)

def extract_skills(src,is_text=False):
    if skill_set is None:
        raise ValueError("Skill_set must be provided for skill extraction from JD.")
    lt = set()

    if is_text:
        src_pre = remove_punctuation(src.lower())
        for skill in skill_set:
            if skill in src_pre:
                lt.add(skill)
    else:
        resume_data = ResumeParser(src).get_extracted_data()
        lt = set(resume_data.get('skills', []))         
    return lt       
