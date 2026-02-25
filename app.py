from flask import Flask, render_template, request, jsonify
import random
app = Flask(__name__)

data = [
    {
        "id" : 0,
        "text" : "Have Chocolate or Vanilla Ice Cream ",
        "optionA" : "Chocolate Ice Cream ",
        "optionB" : "Vanilla Ice Cream ",
    },

    {
        "id" : 1,
        "text" : "Go to the Moves or the Mall ",
        "optionA" : " Movies ",
        "optionB" : " Mall "
    },

    {
        "id" : 2,
        "text" : "Have Tea or Coffee ",
        "optionA" : " Tea ",
        "optionB" : " Coffee "
    },

    {
        "id" : 3,
        "text" : " Sleep In or Wake up Early  ",
        "optionA" : " Sleep In ",
        "optionB" : " Wake Up Early "
    },

    {
        "id" : 4,
        "text" : "Windows or Apple   ",
        "optionA" : " Windows ",
        "optionB" : " Apple ",
    },
]

votes = {
    0:{"A": 0 ,"B": 0},
    1:{"A": 0 ,"B": 0},
    2:{"A": 0 ,"B": 0},
    3:{"A": 0 ,"B": 0},
    4:{"A": 0 ,"B": 0},
}
@app.route("/genQuestion")
def gen_question():
    question = random.choice(data)
    return question

@app.route("/vote")
def vote(id , option):## gets  choice and question id
    if id not in votes:
        raise ValueError("Invalid id")
    if option not in ("A", "B"):
        raise ValueError("Invalid option")
    votes[id][option] += 1

@app.route("/welcome")
def welcome():
    return "<html> <body><h1>!!Welcome To What Would You Rather !! </h1></body></html>"
@app.route("/")
def start_index():
    return render_template("index.html")

app.run(host = "0.0.0.0", port = 423)