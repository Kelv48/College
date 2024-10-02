from flask_wtf import FlaskForm
from wtforms import SubmitField, IntegerField, StringField, RadioField, FloatField
from wtforms.validators import InputRequired, NumberRange


class ShiftForm(FlaskForm):
    plaintext = StringField("Plaintext:",
        validators=[InputRequired()])
    shift = IntegerField("Shift:",
        validators=[InputRequired(), NumberRange(1, 25)])
    ciphertext = StringField("Ciphertext")
    submit = SubmitField("Submit")

class ConversionForm(FlaskForm):
    convert_from = RadioField("From:",
        choices = ["Fahrenheit", "Celsius", "Kelvin"])
    to_convert = FloatField()
    convert_to = RadioField("To",
        choices = ["Fahrenheit", "Celsius", "Kelvin"])
    converted = FloatField()
    submit = SubmitField("Submit")