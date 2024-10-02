from flask import Flask, render_template
from forms import ShiftForm, ConversionForm


app = Flask(__name__)
app.config["SECRET_KEY"] = "i-am-a-secret"

@app.route("/shift", methods=["GET", "POST"])
def shift():
    form = ShiftForm()
    if form.validate_on_submit():
        plaintext = form.plaintext.data
        ciphertext = form.ciphertext.data
        shift = form.shift.data
        ciphertext = ""
        for char in plaintext:
            if char.isupper():
                ciphertext += chr((ord(char) - 65 + shift) % 26 + 65)
            elif char.islower():
                ciphertext += chr((ord(char) - 97 + shift) % 26 + 97)
            else:
                ciphertext += char
        form.ciphertext.data = ciphertext
    return render_template("shift_form.html",
        title="Shift Form",
        form=form)

@app.route("/conversion", methods=["GET", "POST"])
def conversion():
    form = ConversionForm()
    if form.validate_on_submit():
        convert_from = form.convert_from.data
        convert_to = form.convert_to.data
        to_convert = form.to_convert.data
        converted = form.converted.data
        if convert_from == "Fahrenheit":
            if convert_to == "Celsius":
                converted = 5/9 * (to_convert - 32) 
            else:
                converted = 5/9 * (to_convert - 32) + 273
        elif convert_from == "Celsius":
            if convert_to == "Fahrenheit":
                converted = 9/5 * to_convert + 32
            else:
                converted = to_convert + 273
        elif convert_from == "Kelvin":
            if convert_to == "Fahrenheit":
                converted = 9/5 * (to_convert - 273) + 32
            else:
                converted = to_convert - 273
        form.converted.data = converted
    return render_template("conversion_form.html",
    title="Conversion Form",
    form=form)
