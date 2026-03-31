from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/questions')
def questions():
    return render_template('questions.html')


@app.route('/result', methods=['POST'])
def result():
    interest = request.form.get('interest')

    if interest == "coding":
        career = "Software Developer 💻"
    elif interest == "biology":
        career = "Medical / Research 🧬"
    elif interest == "business":
        career = "Business / Entrepreneur 💼"
    elif interest == "design":
        career = "UI/UX Designer 🎨"
    elif interest == "teaching":
        career = "Teacher / Professor 📚"
    elif interest == "sports":
        career = "Sports Professional ⚽"
    elif interest == "music":
        career = "Musician / Artist 🎵"
    elif interest == "government":
        career = "Government Job 🏛️"
    else:
        career = "Explore multiple fields 🔍"

    return render_template('result.html', career=career)


if __name__ == '__main__':
    app.run(debug=True)