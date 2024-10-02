from flask import Flask, render_template
from random import randint

app = Flask(__name__)

@app.route("/rps/<player>")
def rps(player):
    choices = ["rock", "paper","scissors"]
    c = randint(0,2)
    comp = choices[c]
    if comp == "rock" and player == "scissors" or comp == "scissors" and player == "paper" or comp == "paper" and player == "rock":
        outcome = "The player looses"
    elif comp == "rock" and player == "paper" or  comp == "scissors" and player == "rock" or comp == "paper" and player == "scissors":
        outcome = "The player wins"
    elif comp == player:
        outcome = "Its a draw"
    return render_template("rps.html", player=player,comp=comp,outcome=outcome) 

@app.route("/could_it_be_me")
def send_lotto_numbers():
    list_of_numbers = []
    for i in range(0, 6):
        n = randint(1, 47)
        list_of_numbers.append(n)
    return render_template("lotto.html", list_of_numbers=list_of_numbers)

@app.route("/could_it_be_me_two")
def send_lotto_numbers_two():
    list_of_numbers = []
    for i in range(0, 6):
        n = randint(1, 47)
        while n in list_of_numbers:
            n = randint(1, 47)
        list_of_numbers.append(n)
    return render_template("lotto.html", list_of_numbers=list_of_numbers)

@app.route("/rps15/<player>")
def RPS15(player):
    choices = ["rock", "gun", "lightning", "devil", "dragon", "water", "air", "paper", "sponge", "wolf", "tree", "human", "snake", "scissors", "fire"]
    c = randint(0, 14)
    comp = choices[c]
    if comp == "rock" and player in ["fire","scissors","snake","human","wolf","sponge","tree"] or comp == "fire" and player in ["scissors","paper","snake","human","tree","wolf","sponge"] or\
    comp == "scissors" and player in ["air","tree","paper","snake","human","wolf","sponge"] or comp == "snake" and player in ["human","wolf","sponge","tree","paper","air","water"] or\
    comp == "human" and player in ["tree","wolf","sponge","paper","air","water","dragon"] or comp == "tree" and player in ["wolf","dragon","sponge","paper","air","water","devil"] or\
    comp == "wolf" and player in ["sponge","paper","air","water","dragon","lightning","devil"] or comp == "sponge" and player in ["paper","air","water","devil","dragon","gun","lightning"] or\
    comp == "paper" and player in ["air","rock","water","devil","dragon","gun","lightning"] or comp == "air" and player in ["fire","rock","water","devil","gun","dragon","lightning"] or\
    comp == "water" and player in ["devil","dragon","rock","fire","scissors","gun","snake"] or comp == "dragon" and player in ["devil","lightning","fire","rock","scissors","gun","snake"] or\
    comp == "devil" and player in ["rock","fire","scissors","gun","lightning","snakes","human"] or comp == "lightning" and player in ["gun","scissors","rock","tree","fire","snake","human"] or\
    comp == "gun" and player in ["rock","tree","fire","scissors","snake","human","wolf"]:
        outcome = "The player loses"
    elif comp == player:
        outcome = "Its a draw"
    else:
        outcome = "The player wins"
    return render_template("rps.html", player=player,comp=comp,outcome=outcome)
      

   
