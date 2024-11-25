from flask import Flask, request, render_template
from transformers import pipeline

app = Flask(__name__)

qa_model = pipeline("question-answering","distilbert/distilbert-base-cased-distilled-squad")

@app.route("/", methods=["GET", "POST"])
def home():
  if request.method =="GET":
    return render_template("home.html")
  else:
    # get context from the file
    f = open("earth_context.txt", "r")
    context = f.read()

    # get form input 'question'
    question = request.form["question"]

    # get answer from pipeline model
    answer = qa_model(question = question, context = context)

    return render_template("home.html", question = question, answer = answer["answer"])






@app.route("/helloworld")
def hello_world():
  name = "Mike"
  title = "Hello World!"
  message = "Welcome to my first Flask app"
  return render_template("hello.html", title = title, message = message, person = name)

@app.route("/get", methods=["GET"])
def get_request():
  return "GET request"

@app.route("/post", methods=["POST"])
def post_request():
  return "POST request"
