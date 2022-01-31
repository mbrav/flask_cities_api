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
        from .scraper import data_file as cities_rus
        db.create_all()
        print('Loading', len(cities_rus), 'cities into database')

    from .api import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api')

    return app
