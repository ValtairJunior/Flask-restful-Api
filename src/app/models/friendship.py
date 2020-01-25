from app.models import db
from datetime import datetime


class Friendship(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'))
    friend_id = db.Column(db.Integer(), db.ForeignKey('user.id') )
    solicitation = db.Column(db.Boolean(), default=False)
    confirmation = db.Column(db.Boolean(), default=False)
    chat = db.Column(db.Boolean(), default=False)
    create_on = db.Column(db.DateTime(), default=datetime.utcnow())
    update_on = db.Column(db.DateTime(), default=datetime.utcnow(), onupdate=datetime.utcnow())

