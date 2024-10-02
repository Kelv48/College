from flask_wtf import FlaskForm
from wtforms import DecimalField, SubmitField
#other options include StringField, IntegerField,
from wtforms.validators import InputRequired, NumberRange

class BMIForm(FlaskForm):   # a subclass of FlaskForm
    weight = DecimalField("Weight in kg: ",
        validators = [InputRequired(), NumberRange(1, 1000)])
    height = DecimalField("Height in m: ",
        validators = [InputRequired(), NumberRange(1, 1.88)])
    bmi = DecimalField("BMI: ")
    submit = SubmitField("Submit")
