from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class PlayerName(FlaskForm):
    player_name = StringField('Name:', validators=[DataRequired()])
    submit = SubmitField('Start')
