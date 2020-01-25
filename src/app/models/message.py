from app.models import db
from datetime import datetime


class Message(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    friendship_id = db.Column(db.Integer(), db.ForeignKey('friendship.id'))
    message = db.Column(db.Text())
    create_on = db.Column(db.DateTime(), default=datetime.utcnow())
    update_on = db.Column(db.DateTime(), default=datetime.utcnow(), onupdate=datetime.utcnow())