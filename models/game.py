from models.player import *


# changed to choice one ratherthan player 1?±
def game (choice_1, choice_2):
    if choice_1 == "rock" and choice_2 == "scissors":
        return "Player 1 wins!"

    if choice_1 == "scissors" and choice_2 == "paper":
        return "Player 1 wins!"

    if choice_1 == "paper" and choice_2 == "rock":
        return "Player 1 wins!"
    
    if choice_1 == choice_2:
        return 'Draw'

    
    return "Player 2 wins!"