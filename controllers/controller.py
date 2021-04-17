from app import app
from models.game import game, players
from models.player import Player 



@app.route('/')
def index():
    return "Welcome to the Rock,Paper and Scissors game!"
    #return render_template('index.html' title = 'Game',)

@app.route('/<choice_1>/<choice_2>')
def game(choice_1,choice_2):
    

    return f"{game.Player}  wins by playing {Player.choice}"

winner = game(cho 1, ch2
render ())