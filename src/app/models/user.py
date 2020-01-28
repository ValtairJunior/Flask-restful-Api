from app.models import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String())
    email = db.Column(db.String(), unique=True)
    password_hash = db.Column(db.String())
    admin = db.Column(db.Boolean(), default=False)
    create_on = db.Column(db.DateTime(), default=datetime.utcnow())
    update_on = db.Column(db.DateTime(), default=datetime.utcnow(), onupdate=datetime.utcnow())
    
    
    # def check_password(self, password):
    #     return check_password_hash(self.password_hash, password)


    # def set_password(self, password):
    #     self.password_hash = generate_password_hash(password)

   