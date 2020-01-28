from flask import Blueprint
from flask_restful import Api
from flask_cors import CORS
from app.controllers import *

bp = Blueprint('routes', __name__)
api = Api(bp)
CORS(bp)


# api routes using flask restful
api.add_resource(Session, '/session')
api.add_resource(User, '/user')