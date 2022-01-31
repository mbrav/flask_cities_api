import pytest
from flask_cities_api import create_app


@pytest.fixture
def app():
    app = create_app()
    return app


@pytest.fixture
def user(app):
    return 'user'
