from flask import render_template
from app import app
import random

moves = {1: "rock", 2: "scissors", 3: "paper"}


class Game:

    def __init__(self, moves):
        self.moves = moves

    def setup(self, move):
        self.u = move
        if self.u in list(self.moves.values()):
            self.u = list(self.moves.keys())[
                list(self.moves.values()).index(self.u)]
        self.cp = random.choice(list(self.moves.keys()))
        self.cp_name = self.moves[self.cp]
        return self

    def game_check(self):
        self.round_score = self.u - self.cp
        if self.round_score in [-1, 2]:
            return True
        elif self.round_score in [-2, 1]:
            return False
        elif self.round_score == 0:
            return None


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title="Rock Paper Scissors", moves=moves)


@app.route('/moves/<move>')
def moves_list(move):
    single_game = Game(moves)
    cp = single_game.setup(move).cp_name
    return render_template('moves_list.html', title="Rock Paper Scissors", move=move, cp=cp)
