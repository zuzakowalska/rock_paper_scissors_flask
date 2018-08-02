from flask import render_template, request, session
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

    def round_check(self):
        self.round_score = self.u - self.cp
        if self.round_score in [-1, 2]:
            return 1
        elif self.round_score in [-2, 1]:
            return -1
        elif self.round_score == 0:
            return 0


@app.before_request
def session_management():
    session.permanent = True


@app.route('/')
def index():
    session.clear()
    session['game_score'] = 0
    game_score = session['game_score']
    return render_template('index.html', title="Rock Paper Scissors", moves=moves, game_score=game_score)


@app.route('/<move>')
def moves_list(move):
    single_game = Game(moves)
    cp = single_game.setup(move).cp_name
    session['round_score'] = single_game.round_check()
    round_score = session['round_score']
    return render_template('moves_list.html', title="Rock Paper Scissors", move=move, cp=cp, round_score=round_score)


@app.route('/next')
def next_round():
    session['game_score'] += session['round_score']
    game_score = session['game_score']
    if game_score == 3:
        return render_template("win.html")
    elif game_score == -3:
        return render_template("lose.html")
    else:
        return render_template('index.html', title="Rock Paper Scissors", moves=moves, game_score=game_score)
