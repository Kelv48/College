
from flask import Flask, render_template, request


app = Flask(__name__)

#Q1
@app.route("/spy", methods=["GET", "POST"])
def bond():
    if request.method == "GET":
        return render_template("form.html")
    else:
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        return render_template("response.html", 
        first_name=first_name, last_name=last_name)

#Q2
@app.route("/morse" , methods=["GET", "POST"])
def morse():
    if request.method == "GET":
        return render_template("morse_form.html")
    else:
        message = request.form["message"]
        cleaned_message = message.strip().upper()
        morse = ""
        morse_dict = {
            "A": ".-",
            "B": "-...",
            "C": "-.-.",
            " ": "/",
        }
        if message == "":
            return render_template("morse_form.html", message=message, morse="Not known", error="Error: Please fill in the box!")
        for character in cleaned_message:
            if character not in morse_dict:
                return render_template("morse_form.html", cleaned_message=cleaned_message, morse="Not Known", error="Not in the Dictionary")
            code = morse_dict[character]
            morse = morse + code + " "
        return render_template("morse_response.html" , message = message , morse = morse)
        
#Q3
@app.route("/lengths", methods=["GET", "POST"])
def length():
    if  request.method == "GET":
        return render_template("length_form.html",
        inches="", centimetres="", error="")
    else:
        inches = request.form["inches"]
        centimetres = request.form["centimetres"]
        if (inches=="" and centimetres == "") or (inches != "" and centimetres != ""):
            return render_template("length_form.html", inches="", length="", error="Just enter info into one box its not hard")
        if inches != "":
            inches = float(inches)
            centimetres = inches*2.54
        else:
            centimetres = float(centimetres)
            inches = centimetres/2.54
        return render_template("length_form.html", inches=inches,centimetres=centimetres, error="")





            

        
            
       

