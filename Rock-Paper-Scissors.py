from ast import ExtSlice
from math import acosh
from random import randint

a = ["Rock", "Paper", "Scissors"]

machine =a[randint(0,2)]


player = False


while player == False:
    player = input("Rock, Paper, Scissors\n")
    if player == machine:
        print ("Tie!!")
    elif player == "Rock":
        if machine == "Paper":
            print(" You lose!", machine, "covers", player)
        else:
            print("You win!", player, "smashes", machine)

    elif player == "Paper":
        if machine == "Scissors":
            print("You lose", machine, "cuts", player)
        else:
            print('You win', player, "covers", machine)
    elif player == "Scissors":
        if machine == "Rock":
            print("you lose", machine, "smashes", player)
        else:
            print('you win', player, "cuts", machine)
    else:
        print("check you speeling")
    
    player = False
    machine = a[randint(0,2)]