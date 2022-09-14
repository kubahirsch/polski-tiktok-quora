from flask import Flask, render_template
import requests

app = Flask(__name__)

response = requests.get("http://quora.christopher.su/answers/6hARL")
print(response)


@app.get('/')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)