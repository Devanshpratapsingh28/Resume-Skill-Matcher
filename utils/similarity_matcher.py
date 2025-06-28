from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from .text_preprocessing import preprocess_text
from .text_extractor import extract_pdf_text

model = SentenceTransformer('all-MiniLM-L6-v2')

def calc_similarity(resume_path,jd_text):
  
  resume_text = extract_pdf_text(resume_path)
  resume_preprocess_text = preprocess_text(resume_text)
  jd_preprocess_text = preprocess_text(jd_text)
    
  vectors = model.encode([resume_preprocess_text, jd_preprocess_text])
    
  similarity = max(cosine_similarity([vectors[0]], [vectors[1]]),0)
  percentage_similarity = round(similarity[0][0] * 100, 2)
    
  return percentage_similarity


