from flask_sqlalchemy import SQLAlchemy

from . import app


class Region(db.Model):
    """Region database model"""

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)

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

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)

    region_id = db.Column(db.Integer,
                          db.ForeignKey('region.id'),
                          nullable=False)
    region = db.relationship('Region',
                             backref=db.backref('cities', lazy=True))

    def get(self, _id: int):
        ob = City.json(City.query.filter_by(id=_id).first())
        db.session.add(new_object)
        db.session.commit()

    def __init__(self, name: str, region_id: int = None):
        self.name = name
        self.region_id = region_id

    def __repr__(self):
        return f'<city {self.name}>'
