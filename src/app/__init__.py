from flask import Flask
from instance import app_config
from flask_migrate import Migrate
from app.models import db


def _instances_blueprint(app):
    from app.middlewares import bp as middlewares
    app.register_blueprint(middlewares)
    
    from app.models import bp as models
    app.register_blueprint(models)

    from app.routes import bp as routes
    app.register_blueprint(routes)
    

def create_app(config_name):
    app = Flask(__name__,  instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')

    _instances_blueprint(app)
    
    Migrate(app, db)
    
    return app


