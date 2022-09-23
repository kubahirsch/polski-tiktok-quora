from flask import Flask, render_template, request
from scraper.scraper import Scraper
from videocreation.creatingmp3 import create_mp3

app = Flask(__name__)

# response = requests.get("http://quora.christopher.su/answers/6hARL")
# print(response)


question = ''
answers = []
q_a = {}

@app.get('/')
def home():
    return render_template('index.html')

@app.post('/')
def get_link(): 
    global link
    global q_a
    link = request.form.get('link')
    if link == "":
        return render_template('index.html')

    scraper = Scraper()
    
    q_a = scraper.scrape_data(link)
    return render_template('withquestion.html', q_a=q_a)

@app.post('/startgenerating')
def start_generating():
    global question
    global answers
    question = request.form.get('question')
    for i in range(1, len(q_a['answers'])+1):
        answers.append(request.form.get(str(i)))
    text = question
    for i in answers:
        text +=i
    create_mp3(text)
    return render_template('withaudio.html', question=question, answers=answers)

@app.get('/test')
def test_temp():
    return render_template('withaudio.html', question=question, answers=answers )



if __name__ == '__main__':
    app.run(debug=True)