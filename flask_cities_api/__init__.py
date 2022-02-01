from config import config
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import HTTPException

db = SQLAlchemy()


def create_app(config_name):

    app = Flask(__name__)

    app.config.from_object(config['default'])
    config['default'].init_app(app)

    db.init_app(app)

    @app.errorhandler(HTTPException)
    def handle_exception(e):
        """Return JSON instead of HTML for HTTP errors."""
        import json

        response = e.get_response()
        response.data = json.dumps({
            "code": e.code,
            "name": e.name,
            "description": e.description,
        })
        response.content_type = "application/json"
        return response

    @app.before_first_request
    def create_table():
        """Create table on first request and load test data with rus cities"""

        from .models import load_db_data
        from .scraper import data_file as cities_rus

        db.create_all()
        # load_db_data(cities_rus)

    from .api import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api')

    return app
