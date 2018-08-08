from flask import render_template, session, request
from app import app
from app.game import Game
from app.form import PlayerName
from app.ascii import ascii_art

moves = {1: "rock", 2: "scissors", 3: "paper"}


@app.before_request
def session_management():
    session.permanent = True


@app.route('/')
def index():
    session.clear()
    session['game_score'] = 0
    session['round_score'] = 0
    form = PlayerName()
    return render_template('index.html', title="Rock Paper Scissors", form=form)


@app.route('/<move>')
def moves_list(move):
    single_game = Game(moves)
    cp = single_game.setup(move).cp_name
    session['round_score'] = single_game.round_check()
    round_score = session['round_score']
    return render_template('moves_list.html', title="Rock Paper Scissors", move=move, cp=cp, round_score=round_score)


@app.route('/game', methods=['GET', 'POST'])
def game_round():
    if request.method == 'POST':
        player_name = request.form.get('player_name')
    session['game_score'] += session['round_score']
    game_score = session['game_score']
    if game_score == 3:
        return render_template("win.html")
    elif game_score == -3:
        return render_template("lose.html")
    else:
        return render_template('game.html', title="Rock Paper Scissors", moves=moves, game_score=game_score, ascii_art=ascii_art, player_name=player_name)
