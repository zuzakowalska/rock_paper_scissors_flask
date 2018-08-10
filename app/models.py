from app import db


class GameData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))
    score = db.Column(db.Integer)
    win = db.Column(db.Boolean, default=None)

    __mapper_args__ = {
        'confirm_deleted_rows': False
    }

    def __repr__(self):
        data = str(self.id) + ', ' + str(self.name) + ', ' + \
            str(self.score) + ', ' + str(self.win)
        return '<GameData {}>'.format(data)
