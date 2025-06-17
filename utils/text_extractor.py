import PyPDF2 as pypdf

def extract_pdf_text(path):
    text = ""
    with open(path,'rb') as file :
        reader = pypdf.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text()
    
    return text 


