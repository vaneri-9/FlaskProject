from flask import Flask, render_template
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.shortstories


@app.route('/')
def home():
    articles = db.articles.find({})

    return render_template("Home.html", articles=articles)


if __name__ == '__main__':
    app.run()
