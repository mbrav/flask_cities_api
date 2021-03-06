from datetime import datetime

from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash

from . import db


class Region(db.Model):
    """Region database model"""

    __tablename__ = 'regions'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

    cities = db.relationship("City", backref="region", lazy='dynamic')

    def get(self, _id: int):
        ob = Region.json(Region.query.filter_by(id=_id).first())
        db.session.add(new_object)
        db.session.commit()

    def __init__(self, name: str):
        self.name = name

    def __repr__(self):
        return f'<region {self.name}>'


class City(db.Model):
    """City database model"""

    __tablename__ = 'cities'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    population = db.Column(db.Integer, nullable=True)
    year_founded = db.Column(db.Integer, nullable=True)

    region_id = db.Column(db.Integer, db.ForeignKey('regions.id'))

    def get(self, _id: int):
        ob = City.json(City.query.filter_by(id=_id).first())
        db.session.add(new_object)
        db.session.commit()

    def __init__(
            self,
            name: str,
            region_id: int = None,
            population: int = None,
            year_founded: int = None):
        self.name = name
        self.region_id = region_id
        self.population = population
        self.year_founded = year_founded

    def __repr__(self):
        return f'<city {self.name}>'


class User(UserMixin, db.Model):
    """City database model"""

    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    name = db.Column(db.String(64))
    member_since = db.Column(db.DateTime(), default=datetime.utcnow)

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)


def load_db_data(data):
    """Generate database models from pass city data"""

    from tqdm import tqdm

    unique_states = []
    for city in data:
        if city['state'] not in unique_states:
            unique_states.append(city['state'])

    print('Loading', len(unique_states), 'regions into database')
    for state in tqdm(unique_states):
        new_object = Region(name=state)
        db.session.add(new_object)
        db.session.commit()

    print('Loading', len(data), 'cities into database')
    for city in tqdm(data):
        name = city['city']
        state_id = unique_states.index(city['state']) + 1
        population = int(city['population'])
        year_founded = int(city['year-founded'])
        new_object = City(name=name, population=population,
                          year_founded=year_founded, region_id=state_id)
        db.session.add(new_object)
        db.session.commit()
