from flask_wtf import FlaskForm
from wtforms import BooleanField, SubmitField, StringField, SelectField, RadioField
from wtforms.validators import InputRequired


class WombatForm(FlaskForm):
    wombat = BooleanField("Check the box if you think Derek likes wombats: ")
    submit = SubmitField("GO!")

class ToppingForm(FlaskForm):
    #Version 1
    """topping = StringField("What is Derek's fave pizza topping?",
        validators=[InputRequired()])
    submit = SubmitField("GO!")"""
    
    #Version 2
    """topping = SelectField("What is Dereks favourite pizza topping",
        choices = ["anchovies", "caramel", "chocolate", "bacon", "pineapple"],
        validators=[InputRequired()])
    submit = SubmitField("GO!")"""

    #Version 3
    topping = RadioField("What is Dereks favourite pizza topping",
        choices = ["anchovies", "caramel", "chocolate", "bacon", "pineapple"],
        default = "pineapple")
    submit = SubmitField("GO!")


    submit = SubmitField("Submit")