from flask import render_template, session, request, redirect, url_for
from app import app, db
from app.game import Game
from app.models import GameData
from app.form import PlayerName
from app.ascii import ascii_art

moves = {1: "rock", 2: "scissors", 3: "paper"}


@app.before_request
def session_management():
    session.permanent = True


@app.route('/', methods=['GET', 'POST'])
def index():
    form = PlayerName()
    if form.validate_on_submit():
        new_player = GameData(
            player_name=form.player_name.data, player_score=0)
        db.session.add(new_player)
        db.session.commit()
        return redirect('/game')
    return render_template('index.html', title="Rock Paper Scissors", form=form)


@app.route('/<move>')
def moves_list(move):
    player = GameData.query.filter_by(
        player_name=GameData.player_name).order_by(GameData.id.desc()).first()
    single_game = Game(moves)
    cp = single_game.setup(move).cp_name
    round_score = single_game.round_check()
    player.player_score = player.player_score + round_score
    db.session.commit()
    return render_template('moves_list.html', title="Rock Paper Scissors", move=move, cp=cp, round_score=round_score)


@app.route('/game', methods=['GET', 'POST'])
def game_round():
    player = GameData.query.filter_by(
        player_name=GameData.player_name).order_by(GameData.id.desc()).first()
    player_name = player.player_name
    player_score = player.player_score
    if player_score == 3:
        return render_template('win.html', title="Rock Paper Scissors", player_name=player_name)
    elif player_score == -3:
        return render_template('lose.html', title="Rock Paper Scissors", player_name=player_name)
    else:
        return render_template('game.html', title="Rock Paper Scissors", moves=moves, player_score=player_score, ascii_art=ascii_art, player_name=player_name)


@app.route('/new-game')
def new_game():
    session.clear()
    return redirect('/')
