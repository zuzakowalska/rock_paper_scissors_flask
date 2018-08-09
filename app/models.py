from app import db


class GameData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    player_name = db.Column(db.String(32))
    player_score = db.Column(db.Integer)

    __mapper_args__ = {
        'confirm_deleted_rows': False
    }

    def __repr__(self):
        return self.player_name
