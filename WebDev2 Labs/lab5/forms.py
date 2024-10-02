from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import NumberRange, InputRequired

class GuessForm(FlaskForm):
    guess = IntegerField("Please guess a number between 1 and 100 inclusive",
                          validators=[InputRequired(), NumberRange(1, 100)])
    submit = SubmitField("Submit")