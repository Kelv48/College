from flask import Flask, session, render_template, redirect, url_for
from flask_session import Session
from forms import GuessForm
from random import randint

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config["SECRET_KEY"] = "i-am-a-secret"
Session(app)

@app.route("/guess", methods=["GET", "POST"])
def guess():
    form = GuessForm()
    outcome=""
    number = None
    if "number" not in session:
        number = randint(1,100)
        session["number"] = number
    if form.validate_on_submit():
        guess = form.guess.data
        if session["number"] == guess:
            number = randint(1,100)
            session["number"] = number
            return render_template("guess.html", form=form, outcome="You guessed right", number=number, secret_number=session["number"])
        elif session["number"] > guess:
            return render_template("guess.html", form=form, outcome="Guess Higher", number=number, secret_number=session["number"])
        elif session["number"] < guess:
            return render_template("guess.html", form=form, outcome="Guess Lower", number=number, secret_number=session["number"])
    return render_template("guess.html", form=form, outcome=outcome, number="")
       
