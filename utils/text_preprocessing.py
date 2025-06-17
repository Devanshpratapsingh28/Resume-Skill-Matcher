import string
import spacy

# spaCy English model
nlp = spacy.load('en_core_web_sm')

punct = string.punctuation

def lowercasing(text):
    return text.lower()

def remove_punctuation(text):
    return text.translate(str.maketrans('', '', punct))

def lemmantize(text):
    doc = nlp(text)
    tokens = [word.lemma_ for word in doc if word.is_alpha] 
    return ' '.join(tokens)

def preprocess_text(text):
    text = lowercasing(text)
    text = remove_punctuation(text)
    text = lemmantize(text)
    return text
