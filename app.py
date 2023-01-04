from flask import Flask, render_template, request
from flask_cors import CORS
import requests
import json
import inspect

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    token = request.cookies.get('token');
    articles = {}
    if token != None:
        articles = requests.post('http://localhost:3001/articles', headers={"Content-type": "application/json; charset=UTF-8"}, data={'token': token})
    else:
        articles = requests.post('http://localhost:3001/articles', headers={"Content-type": "application/json; charset=UTF-8"}, data={})

    print(token)
    print(articles)
    print(articles.text)
    print(articles.headers)
    print(inspect.getmembers(articles))
    #print(articles.body)

    return render_template("Home.html", articles=articles.text)


if __name__ == '__main__':
    app.run()
