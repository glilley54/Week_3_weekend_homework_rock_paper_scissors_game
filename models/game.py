from models.player import *

player1 = ("John", "rock")
player2 = ("Andrew, scissors")

players = [player1,player2]

# changed to choice one ratherthan player 1?±
def game (choice_1, choice_2):
    if player1.choice == "rock" and player2.choice == "scissors":
        return player1 # put string player 1 wins!

    if player1.choice =="scissors" and player2.choice == "paper":
        return player1

    if player1.choice == "paper" and player2.choice == "rock":
        return player1
    
    if player1.choice == player2.choice:
        return None

    return player2