from flask import Flask, render_template, request
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re

app = Flask(__name__)

# -----------------------------
# Text utilities
# -----------------------------
def normalize_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s]', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def extract_keywords(text):
    return set(normalize_text(text).split())

# -----------------------------
# Core grading logic
# -----------------------------
def calculate_score(student, teacher, max_score):
    if not student.strip() or not teacher.strip():
        return 0, []

    student = normalize_text(student)
    teacher = normalize_text(teacher)

    teacher_keywords = extract_keywords(teacher)
    student_keywords = extract_keywords(student)

    # If no meaningful keywords → zero marks
    if len(teacher_keywords) == 0 or len(student_keywords) == 0:
        return 0, list(teacher_keywords)

    matched = teacher_keywords.intersection(student_keywords)
    missed = teacher_keywords - student_keywords

    coverage_ratio = len(matched) / len(teacher_keywords)

    similarity = 0
    try:
        vectorizer = TfidfVectorizer(stop_words="english")
        vectors = vectorizer.fit_transform([teacher, student])
        similarity = cosine_similarity(vectors[0:1], vectors[1:2])[0][0]
    except ValueError:
        similarity = 0

    final_score = round(
        (coverage_ratio * 0.6 + similarity * 0.4) * max_score,
        2
    )

    # Totally irrelevant answer
    if coverage_ratio < 0.15 and similarity < 0.15:
        final_score = 0

    return final_score, sorted(list(missed))

# -----------------------------
# Routes
# -----------------------------
@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        # SAFE form reading (NO crashes)
        student_answer = request.form.get("student_answer", "")
        teacher_answer = request.form.get("teacher_answer", "")
        rubrics = request.form.get("rubrics", "")
        max_score = request.form.get("max_score", "0")

        try:
            max_score = float(max_score)
        except:
            max_score = 0

        score, missed_points = calculate_score(
            student_answer,
            teacher_answer,
            max_score
        )

        percentage = (score / max_score * 100) if max_score > 0 else 0

        if percentage >= 75:
            grade_class = "good"
        elif percentage >= 40:
            grade_class = "average"
        else:
            grade_class = "bad"

        result = {
            "score": score,
            "max_score": max_score,
            "missed": missed_points,
            "grade_class": grade_class,
            "percentage": round(percentage, 2)
        }

    return render_template("index.html", result=result)

# -----------------------------
# App runner
# -----------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)