from config import config
from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
ma = Marshmallow()


def create_app(config_name):

    app = Flask(__name__)

    test = config['default']

    app.config.from_object(config['default'])
    config['default'].init_app(app)

    db.init_app(app)
    ma = Marshmallow(app)

    @app.before_first_request
    def create_table():
        db.create_all()

    from .api import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api')

    return app
