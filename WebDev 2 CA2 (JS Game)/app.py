from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/game")
def game():
    return render_template("game.html")

@app.route("/controls")
def controls():
    return render_template("controls.html")

@app.route("/credits")
def credits():
    return render_template("credits.html")