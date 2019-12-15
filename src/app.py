from flask import Flask
from .game import Game

import random

app = Flask(__name__)

# singleton real bad but whatever
the_game = None

@app.route('/creategame')
def create_game():
    the_game = Game()
    the_game.start_game()
    print(the_game.hand_state)
    return "Game {} created".format(the_game.id)

@app.route('/state')
def get_state():
    the_state = HandState(p1_stack=20000, p2_stack=20000, big_blind=200, p1_button=True)
    print(the_state)
    return "{}".format(the_state)
