from flask import Flask
from datetime import datetime
from random import choice

app = Flask(__name__)

@app.route("/")
def send_greeting():
    return "Hello, world!"

@app.route("/tell_time")
def send_current_date_time():
    return datetime.now().strftime("%H:%M:%S %d-%m-%y")

@app.route("/greet_me")
def send_random_greeting():
    phrases = ["my friend", "bad ass", "ya big eejit", "you sad sap"]
    return "Hello, " + choice(phrases)

@app.route("/greet_by_name/<name>")
def send_greeting_by_name(name):
    return "Hello, " + name

@app.route("byebye/<name>")
@app.route("/farewell/<name>")
def send_parting_by_name(name):
    return "Goodbye, " + name

@app.errorhandler(404)
def page_not_found(error):
    return "Get out of here", 404
