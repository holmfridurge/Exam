import exam as ex
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/getTriviaQuestions/")
def triviaQuest():
    return "Here are your questions"

@app.route("/getQuestions/")
def quest():
    return "Insert your own questions"

if __name__ == "__main__":
    app.run()
