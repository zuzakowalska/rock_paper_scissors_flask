from flask import render_template, request, session
from app import app
from app.Game import Game

MOVES = {1: "rock", 2: "scissors", 3: "paper"}


@app.before_request
def session_management():
    session.permanent = True


@app.route('/')
def index():
    session.clear()
    session['game_score'] = 0
    game_score = session['game_score']
    return render_template('index.html', title="Rock Paper Scissors",
                           moves=MOVES, game_score=game_score)


@app.route('/<move>')
def moves_list(move):
    single_game = Game(MOVES)
    cp = single_game.setup(move).cp_name
    session['round_score'] = single_game.round_check()
    round_score = session['round_score']
    return render_template('moves_list.html', title="Rock Paper Scissors",
                           move=move, cp=cp, round_score=round_score)


@app.route('/next')
def next_round():
    session['game_score'] += session['round_score']
    game_score = session['game_score']
    if game_score == 3:
        return render_template("win.html")
    elif game_score == -3:
        return render_template("lose.html")
    else:
        return render_template('index.html', title="Rock Paper Scissors",
                               moves=MOVES, game_score=game_score)
