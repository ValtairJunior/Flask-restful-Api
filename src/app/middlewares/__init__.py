from app.middlewares.auth import encoded_token, decode_token
from flask import Blueprint


bp = Blueprint('middlewares', __name__)



