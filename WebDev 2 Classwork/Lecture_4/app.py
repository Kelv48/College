from flask import Flask, render_template, request

app = Flask(__name__)


"""
@app.route("/form")
def send_form():
    return render_template("form.html")

@app.route("/response", methods=["POST"])
def send_response():
    given_name = request.form["given_name"]
    family_name = request.form["family_name"]
    return render_template("response.html", 
    given_name=given_name, family_name=family_name)
"""

@app.route("/greet_me", methods=["GET", "POST"])
def greet():    
    if request.method == "GET":
        return render_template("form.html")
    else:
        given_name = request.form["given_name"]
        family_name = request.form["family_name"]
        return render_template("response.html", 
        given_name=given_name, family_name=family_name)
