from flask import Flask, render_template
from forms import BMIForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "i-am-a-secret"


#The former code not fully fool proof ;)
"""@app.route("/bmi", methods=["GET", "POST"])
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
        try:
        weight = float(weight)
        height = float(height)
        if weight < 1 or weight > 1000 or height < 1 or height > 1.88:
            return render_template("bmi_form.html",
            weight=weight, height=height, bmi="", error="Error: Please use sensible numbers!")
        bmi = weight / (height * height)
        return render_template("bmi_response.html", 
        weight=weight, height=height, bmi=bmi, error="")"""




#This and the following are essentially the same   V1
"""@app.route("/bmi", methods=["GET", "POST"])
def bmi():    
    if request.method == "GET":
        return render_template("bmi_form.html",
        weight="", height="" ,bmi="", error="")   
    else:                                           
        weight = request.form["weight"]
        height = request.form["height"]
        weight = float(weight)
        height = float(height)
        bmi = weight / (height * height)
        return render_template("bmi_response.html", 
        weight=weight, height=height, bmi=bmi, error="")"""
#This removes the else part to shorten the code    V2
@app.route("/bmi", methods=["GET", "POST"])
def bmi():    
    form = BMIForm()
    if form.validate_on_submit():
        weight = form.weight.data
        height = form.height.data
        bmi = weight / (height * height)
        form.bmi.data = bmi
    return render_template("bmi_form.html", form=form) 
       