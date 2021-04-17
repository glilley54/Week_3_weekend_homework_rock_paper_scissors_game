from flask import render_template
from app import app
from models.game import game
from models.player import Player 



@app.route('/')
def index():
    return render_template('index.html', title= 'Game')

@app.route('/<choice_1>/<choice_2>')
def result(choice_1,choice_2):
    game(choice_1,choice_2)
    winner = game(choice_1,choice_2)
    return render_template('index.html', title= 'Game', winner = winner)

    

    #return f"{game.Player}  wins by playing {Player.choice}"

#winner = game(cho 1, ch2
#render ())