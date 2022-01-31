# run.py

import os

from flask_cities_api import create_app

if __name__ == '__main__':
    config = os.getenv('FLASK_CONFIG') or 'default'
    app = create_app(config)
    app.run()
