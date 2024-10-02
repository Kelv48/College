from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired



class WinnerForm(FlaskForm):
    choice = StringField("Country:", validators=[InputRequired()])
    submit = SubmitField("Submit")

class Min_WinnerForm(FlaskForm):
    choice = StringField("Country:")
    points = StringField("Points:")
    submit = SubmitField("Submit")










