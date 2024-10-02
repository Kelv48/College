from flask import Flask, session, render_template, redirect, url_for
from flask_session import Session
from database import get_db, close_db

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
app.teardown_appcontext(close_db)

@app.route("/wines")
def wines():
    db = get_db()
    wines = db.execute("""SELECT * FROM wines;""").fetchall()
    return render_template("wines.html", wines=wines)

@app.route("/wine/<int:wine_id>")
def wine(wine_id):
    db = get_db()
    wine = db.execute("""SELECT * FROM wines
                         WHERE wine_id = ?;""", (wine_id,)).fetchall()
    return render_template("wine.html", wine=wine)
                          
@app.route("/cart")
def cart():
    if "cart" not in session:
        session["cart"] = {}
    return render_template("cart.html", cart=session["cart"])

@app.route("/add_to_cart/<int:wine_id>")
def add_to_cart(wine_id):
    if "cart" not in session:
        session["cart"] = {}
    if wine_id not in session["cart"]:
        session["cart"][wine_id] = 1
    else:
        session["cart"][wine_id] = session["cart"][wine_id] + 1
    return redirect(url_for("cart"))