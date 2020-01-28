from flask import Flask
from instance import app_config
from flask_migrate import Migrate
from app.models import config_db


def _instances_blueprint(app):
    from app.middlewares import bp as middlewares
    app.register_blueprint(middlewares)
    
    from app.models import bp as models
    app.register_blueprint(models)

    from app.routes import bp as routes
    app.register_blueprint(routes)
    

def create_app():
    app = Flask(__name__,  instance_relative_config=True)
    app.config.from_object(app_config['development'])
    app.config.from_pyfile('config.py')

 # config_db(app)
    with app.app_context():
        config_db(app)

    _instances_blueprint(app)
    
    Migrate(app, app.db)
    
    return app


