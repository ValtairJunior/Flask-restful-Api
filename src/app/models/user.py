from app.models import db
from datetime import datetime


class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String())
    email = db.Column(db.String(), unique=True)
    password_hash = db.Column(db.String())
    admin = db.Column(db.Boolean())
    create_on = db.Column(db.DateTime(), default=datetime.utcnow())
    update_on = db.Column(db.DateTime(), default=datetime.utcnow(), onupdate=datetime.utcnow())