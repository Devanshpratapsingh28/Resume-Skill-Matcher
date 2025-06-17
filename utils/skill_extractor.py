import csv
from pyresparser import ResumeParser
from text_preprocessing import remove_punctuation
def create_skills_set(path):
    try :
        with open(path,'r',encoding='utf-8') as file :
            reader = csv.reader(file)
            for row in reader : 
                lt = [skill.strip().lower() for skill in row if skill.strip()]
            return set(lt)
    except FileNotFoundError:
        raise FileNotFoundError(f"CSV file not found")

skill_set = create_skills_set('/Users/devanshpratap28/Documents/TBD/static/skills.csv')

def extract_skills(src,is_text=False):
    if skill_set is None:
        raise ValueError("skill_set must be provided")
    lt = set()
    if is_text :
        src_pre = remove_punctuation(src.lower())
        for skill in skill_set:
            if skill in src_pre:
                lt.add(skill)


    else :
        val = ResumeParser(src).get_extracted_data()
        lt = set(val.get('skills',[]))

    return lt       
