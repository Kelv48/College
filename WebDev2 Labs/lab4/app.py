from flask import Flask, render_template
from database import get_db, close_db
from forms import WinnerForm, Min_WinnerForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "i-am-a-secret"
app.teardown_appcontext(close_db)

@app.route("/winners" ,methods=["GET","POST"])
def winners():
    form = WinnerForm()
    winner = None
    if form.validate_on_submit():
        choice = form.choice.data
        choice = choice.lower()
        choice = choice.title()
        db = get_db()
        winner = db.execute("""SELECT * FROM winners
                               WHERE country = ?;""", (choice,)).fetchall()
        if winner != list():
            return render_template("winners.html", form=form, winners=winner)
        else:
             form.choice.errors.append("Not in the database")
    return render_template("winners.html", form=form)
        
@app.route("/min_winners", methods=["GET","POST"])
def min_winners():
     form = Min_WinnerForm()
     choice = None
     points = None
     if form.validate_on_submit():
          choice = form.choice.data
          points = form.points.data
          choice = choice.lower() # user_data validation incase a user has random capitalization
          choice = choice.title() #user_data validation to ensure that if the user enters countries in all lower case it fixes the result
          db = get_db()
          if points is "" and choice is "":
            option4 = db.execute("""SELECT * 
                                    FROM winners""").fetchall() #if the user enters neither, the table contains all winners.
            if option4 != list(): #user data validation to check if the country entered is in the database
                return render_template("Min_winners.html", form=form, winners=option4)
            else:
             form.choice.errors.append("Not in the database")
            
          elif choice is not None and points is "":
            option1 = db.execute("""SELECT * FROM winners
                               WHERE country = ?;""", (choice,)).fetchall() #If the user enters a country but no points, the table contains winners from that country;
            if option1 != list(): #user data validation to check if the country entered is in the database
                return render_template("Min_winners.html", form=form, winners=option1)
            else:
             form.choice.errors.append("Not in the database")

          elif points is not None and choice is "":
            option2 = db.execute("""SELECT * FROM winners
                               WHERE points >= ?;""", (points,)).fetchall() #if the user enters points but no country, 
            if option2 != list():                                           #the table contains winners who achieved at least that many points;
                return render_template("Min_winners.html", form=form, winners=option2)
            else:
             form.choice.errors.append("Not in the database")
            
          elif points is not None and choice is not None:
            option3 = db.execute("""SELECT * FROM winners
                               WHERE country = ? and points >= ?;""", (choice, points)).fetchall() #if the user enters a country and points, the table contains winners 
            if option3 != list():                                                                  #from that country who achieved at least that many points;
                return render_template("Min_winners.html", form=form, winners=option3)
            else:
             form.choice.errors.append("Not in the database")
            
     return render_template("Min_winners.html", form=form)







