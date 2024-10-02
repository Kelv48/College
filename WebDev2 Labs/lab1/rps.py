from random import randint
from secrets import choice

def rps(player):
    choices = ["rock", "paper","scissors"]
    c = randint(0,2)
    choice = choices[c]
    if choice == player:
        return "Its a draw"
    else:
        return "rps.py"

pick = str(input("Enter a choice "))
result = rps(pick)
print(result)