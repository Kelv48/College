from flask import Flask, render_template, make_response, request
from forms import VoteForm


app = Flask(__name__)
app.config["SECRET_KEY"] = "i-am-a-secret"

app.route("/vote", methods=["GET", "POST"])
def vote():
    if request.cookies.get("voted") == "yes":
        return render_template("feedback.html", message="Sorry! But you've already voted.")
    form = VoteForm()
    if form.validate_on_submit():
        vote = form.vote.data

        response = make_response(render_template("feedback.html", 
            message="Thanks for your vote!"))
        response.set_cookie("voted", "yes", max_age=5*365*24*60*60)
        return response
    return render_template("vote_form.html", form=form)