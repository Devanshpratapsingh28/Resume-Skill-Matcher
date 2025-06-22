import os
from dotenv import load_dotenv
from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
from werkzeug.exceptions import RequestEntityTooLarge
from config import Config
from tempfile import NamedTemporaryFile as tmpfile
from utils.similarity_matcher import calc_similarity
from utils.feedback import missing_skills

app = Flask(__name__)
app.config.from_object(Config)

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

def allowed_file(filename):
    ext = filename.rsplit('.', 1)[-1].lower()
    return ext in app.config['ALLOWED_EXTENSIONS']

@app.errorhandler(RequestEntityTooLarge)
def handle_large_file(error):
    return render_template('index.html'), 413

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        file = request.files['resume']
        jd = request.form['jd']

        if file.filename == '': 
            return render_template('index.html')

        if not allowed_file(file.filename):
            return render_template('index.html')

        filename = secure_filename(file.filename)
        try:
            with tmpfile(delete=False, suffix=os.path.splitext(filename)[1]) as temp:
                file.save(temp.name)
                temp_path = temp.name

            result = helper(temp_path, jd)

        finally:
            if os.path.exists(temp_path):
                os.remove(temp_path)

        return render_template(
            'result.html',
            name=name,
            similarity_score=result['similarity_score'],
            feedback=result['feedback']
        )

    return render_template('index.html')

def helper(resume_path, jd):
    score = calc_similarity(resume_path, jd)
    skills_lack = missing_skills(resume_path, jd)

    flag = bool(skills_lack)

    if score < 70:
        feedback = "Your resume is not a strong match for the job description."
        if flag:
            feedback += f" You are missing the following key skills: {', '.join(skills_lack)}."

    elif score < 90:
        feedback = "Your resume is a decent match for the job description."
        if flag:
            feedback += f" You could improve it further by adding the following skills: {', '.join(skills_lack)}."

    else:
        feedback = "Your resume is a great match for the job description. Keep up the good work!"

    return {
        'similarity_score': score,
        'feedback': feedback
    }

if __name__ == "__main__":
    app.run(debug=True)
