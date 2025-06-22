# 🧠 Resume Skill Matcher

### 🚀 Aim
Create an NLP-based web app that assesses resume-job fit using semantic similarity and highlights missing skills.



---

## ✅ Features

- 📊 Calculate similarity score between Resume and JD.  
- 📋 Provide skill-based feedback for resume improvement.  
- 🖼️ Clean, responsive UI with modern design.  
- 📄 Supports `.pdf`resume files.

---

## 🛠️ Tech Stack

### 🔹 Backend:
- **Python**
- **Flask**

### 🔹 NLP & Machine Learning
- [`spaCy`](https://spacy.io) – Text preprocessing and lemmatization  
- [`sentence-transformers`](https://www.sbert.net) – Semantic vector embeddings  
- [`scikit-learn`](https://scikit-learn.org) – Cosine similarity computation  

### 🔹 Resume Parsing
- [`ResumeParser`](https://pypi.org/project/ResumeParser/) – Skill extraction  
- [`PyPDF2`](https://pypi.org/project/PyPDF2/) – PDF text extraction  

### 🔹 Utilities
- `tempfile`, `os`, `dotenv`, `werkzeug` – Secure file handling and configuration  

### 🔹 Frontend
- HTML + CSS – Modern glass-style UI

---

## 📦 Installation & Setup

### 🔧 Run Locally

```bash
# Clone the repository
git clone https://github.com/your-username/resume-skill-matcher.git
cd resume-skill-matcher

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate        # Linux/macOS
venv\Scripts\activate           # Windows

# Install all dependencies
pip install -r requirements.txt

# Start the Flask server
python app.py
```

## 🔮 Upcoming Features

- 🎯 **Personalized Feedback**  
  Tailored suggestions based on missing skills to help candidates optimize their resumes for specific job descriptions.

- 🧾 **Expanded File Format Support**  
  Support for additional resume formats such as `.doc`, `.txt`, and `.rtf` to improve flexibility and accessibility.



## 📚 Open-Source Utilities
[![Scikit-learn](https://img.shields.io/badge/-Scikit--learn-F7931E?logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![Jupyter Notebook](https://img.shields.io/badge/-Jupyter%20Notebook-F37626?logo=jupyter&logoColor=white)](https://jupyter.org/)



