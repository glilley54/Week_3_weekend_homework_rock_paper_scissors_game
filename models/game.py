import models.player import *

player1 = ("John", "rock")
player2 = ("Andrew, Scissors")

def game (player1,player2):
    if player1.choice == "rock" and player2.choice == "scissors":
        return player1

    if player1.choice =="scissors" and player2.choice == "paper":
        return player1

    if player1.choice == "paper" and player2.choice == "rock":
        return player1
    
    if player1.choice == player2.choice:
        return None

    return player2
