from datetime import datetime

from flask import Flask, Response, jsonify, redirect, request
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flask_cities_api.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

ma = Marshmallow(app)


@app.before_first_request
def create_table():
    db.create_all()


class Region(db.Model):
    """Region database model"""

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)

    def get(self, _id: int):
        ob=Region.json(Region.query.filter_by(id=_id).first())
        db.session.add(new_object)
        db.session.commit()

    def __init__(self, name: str):
        self.name=name

    def __repr__(self):
        return f'<region {self.name}>'


class RegionSchema(ma.Schema):
    """Region schema"""

    class Meta:
        fields=('id', 'name')


class City(db.Model):
    """City database model"""

    id=db.Column(db.Integer, primary_key = True)
    name=db.Column(db.String(100), unique = True)

    region_id=db.Column(db.Integer,
                          db.ForeignKey('region.id'),
                          nullable = False)
    region=db.relationship('Region',
                             backref = db.backref('cities', lazy=True))

    def get(self, _id: int):
        ob=City.json(City.query.filter_by(id=_id).first())
        db.session.add(new_object)
        db.session.commit()

    def __init__(self, name: str, region_id: int = None):
        self.name=name
        self.region_id=region_id

    def __repr__(self):
        return f'<city {self.name}>'


class CitySchema(ma.Schema):
    """City schema"""

    class Meta:
        fields=('id', 'name', 'region_id')


city_schema=CitySchema()
cities_schema=CitySchema(many = True)
region_schema=RegionSchema()
regions_schema=RegionSchema(many = True)


@ app.route('/cities', methods = ['GET', 'POST'])
def cities():
    """Cities route"""

    if request.method == 'GET':
        all_cities=City.query.all()
        result=cities_schema.dump(all_cities)

        return jsonify({'cities': result})

    if request.method == 'POST':
        name=request.json['name']
        region_id=request.json['region_id']

        new_object=City(name, region_id)

        db.session.add(new_object)
        db.session.commit()
        return city_schema.jsonify(new_object)


@ app.route('/regions', methods = ['GET', 'POST'])
def regions():
    """Regions route"""

    if request.method == 'GET':
        all_regions=Region.query.all()
        result=regions_schema.dump(all_regions)

        return jsonify({'regions': result})

    if request.method == 'POST':
        name=request.json['name']

        new_object=Region(name)

        db.session.add(new_object)
        db.session.commit()
        return region_schema.jsonify(new_object)


if __name__ == '__main__':
    app.run(debug = True)
