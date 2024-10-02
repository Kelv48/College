from flask import Flask, render_template
from database import get_db, close_db
from forms import BandForm



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
    form = BandForm
    gigs = None
    if form.validate_on_submit():
        band = form.band.data
        db = get_db()
        gigs = db.execute("""SELECT * FROM gigs
                            WHERE gig_date >= DATE('now')
                            AND band = ?;""" % (band,) ).fetchall() 
    #What comes back is a list of dictionaries
    return render_template("gigs_form.html", form=form, gigs=gigs) 





