from app.middlewares.auth import encoded_token, decode_token
from flask import Blueprint
from flask_marshmallow  import Marshmallow

bp = Blueprint('middlewares', __name__)

ma = Marshmallow()

ma.init_app(bp)
