from operator import index
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
    global answers
    global question
    link = request.form.get('link')
    if link == "":
        return render_template('index.html')

    scraper = Scraper()
    
    q_a = scraper.scrape_data(link)
    for i in q_a['answers']:
        answers.append(i)
    question = q_a['question']
    
    return render_template('withquestion.html', answers=answers, question=question)

@app.post('/startgenerating')
def start_generating():
    global question
    global answers
    question = request.form.get('question')
    text = question
    index_of_answers_to_use = request.form.getlist('using')
    index_of_answers_to_use = [int(i) for i in index_of_answers_to_use]
    
    for j in range(len(answers)):
        answers[j] = request.form.get(answers[j])
        text+=answers[j]
    
    for i in sorted(answers, reverse=True):
        if answers.index(i) not in index_of_answers_to_use:
            answers.remove(i)
    # create_mp3(text)
    print(index_of_answers_to_use)
    return render_template('withaudio.html', question=question, answers=answers)



if __name__ == '__main__':
    app.run(debug=True)