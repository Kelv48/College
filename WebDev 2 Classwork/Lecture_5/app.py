from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/morse", methods=["GET", "POST"])
def morse():    
    if request.method == "GET":
        return render_template("morse_form.html")
    else:
        message = request.form["message"]
        cleaned_message = message.strip().upper()
        morse=""
        morse_dict= {
            "A": ".-",
            "B": "-...",
            "C": "-.-.",
            " ": "/"
        }
        for character in cleaned_message:
            code = morse_dict[character]
            morse = morse + code + " "
        return render_template("morse_response.html", 
        message=message, morse=morse)





@app.route("/bmi", methods=["GET", "POST"])
def bmi():    
    if request.method == "GET":
        return render_template("bmi_form.html",
        weight="", height="" ,bmi="", error="")   
    else:                                           
        weight = request.form["weight"]
        height = request.form["height"]
        if weight == "" or height == "":
            return render_template("bmi_form.html",
            weight=weight, height=height, bmi="", error="Error: Please fill in both boxes!")
        weight = float(weight)
        height = float(height)
        if weight < 1 or weight > 1000 or height < 1 or height > 1.88:
            return render_template("bmi_form.html",
            weight=weight, height=height, bmi="", error="Error: Please use sensible numbers!")
        bmi = weight / (height * height)
        return render_template("bmi_response.html", 
        weight=weight, height=height, bmi=bmi, error="")
