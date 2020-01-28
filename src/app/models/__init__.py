from flask import Blueprint
from flask_sqlalchemy import SQLAlchemy


bp = Blueprint('models', __name__)

db = SQLAlchemy()

def config_db(app):
    db.init_app(app)
    app.db = db


from app.models import *

