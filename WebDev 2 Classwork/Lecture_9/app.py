from flask import Flask, render_template
from database import get_db, close_db
from forms import BandForm, GigForm, RegistrationForm
from datetime import datetime
from werkzeug.security import generate_password_hash



app = Flask(__name__)
app.config["SECRET_KEY"] = "i-am-a-secret"
app.teardown_appcontext(close_db)           #whenever a route finishes this line automatically closes the connection 

@app.route("/all_gigs") #only uses get requests
def all_gigs():
    db = get_db()
    gigs = db.execute("""SELECT * FROM gigs;""").fetchall() 
    #What comes back is a list of dictionaries
    return render_template("gigs.html", gigs=gigs) 


@app.route("/future_gigs") #only uses get requests
def future_gigs():
    db = get_db()
    gigs = db.execute("""SELECT * FROM gigs
                         WHERE gig_date >= DATE('now');""").fetchall() 
    #What comes back is a list of dictionaries
    return render_template("gigs.html", gigs=gigs) 

@app.route("/future_gigs_by_band", methods=["GET","POST"]) #only uses get requests
def future_gigs_by_band():
    form = BandForm()
    gigs = None
    if form.validate_on_submit():
        band = form.band.data
        db = get_db()
        gigs = db.execute("""SELECT * FROM gigs
                            WHERE gig_date >= DATE('now')
                            AND band = ?;""" , (band,) ).fetchall() 
    #What comes back is a list of dictionaries
    return render_template("gigs_form.html", form=form, gigs=gigs) 


@app.route("/insert_gig", methods=["GET","POST"]) #only uses get requests
def insert_gig():
    form = GigForm()
    message = ""
    if form.validate_on_submit():
        band = form.band.data
        gig_date = form.gig_date.data
        if gig_date <= datetime.now().date():
            form.gig_date.errors.append("Date must be in the future")
        else:
            db = get_db()
            clashing_gig = db.execute("""SELECT * FROM gigs
                                         WHERE gig_date = ?;""", (gig_date,)).fetchone()
            if clashing_gig is not None:
                form.gig_date.errors.append("Gig date clashes with another")
            else:
                db.execute("""INSERT INTO gigs (band, gig_date)
                      VALUES (?, ?)""", (band, gig_date))
            #The db.commit command is there to ensure any changes to the database are actually carried out
            db.commit()
            message = "New gig successfully inserted"
    return render_template("insert_gig.html", form=form, message=message)


@app.route("/register", methods=["GET","POST"]) #only uses get requests
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user_id = form.user_id.data
        password = form.password.data
        password2 = form.password2.data
        db = get_db()
        clashing_user = db.execute("""SELECT * FROM users
                                      WHERE user_id = ?;""", (user_id,)).fetchone()
        if clashing_user is not None:
            form.user_id.errors.append("User id clashes with another")
        else:
            db.execute("""INSERT INTO users (user_id, password)
                      VALUES (?, ?)""", (user_id, generate_password_hash(password)))
            db.commit()
            return "Unfinished (redirect to login)"
    return render_template("register.html", form=form)





