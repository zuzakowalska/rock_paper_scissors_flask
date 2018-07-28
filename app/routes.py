from flask import render_template
from app import app
import random

moves = {1: "rock", 2: "scissors", 3: "paper"}


def round(moves, move):
    while True:
        u = move
        if u in list(moves.values()):
            u = list(moves.keys())[list(moves.values()).index(u)]
            break
    cp = random.choice(list(moves.keys()))
    game_check = u - cp
    if game_check in [-1, 2]:
        return True
    elif game_check in [-2, 1]:
        return False


def game():
    score = 0
    while -3 < score < 3:
        if round(moves, move):
            score += 1
        else:
            score -= 1
    if score == -3:
        return "You lose"
    elif score == 3:
        return "You win"


@app.route('/')
@app.route('/index')
def index():

    return render_template('index.html', title="Rock paper Scissors", moves=moves)


@app.route('/moves/<move>')
def moves_list(move):
    round_score = round(moves, move)
    return render_template('moves_list.html', title="Rock paper Scissors", move=move, round_score=round_score)