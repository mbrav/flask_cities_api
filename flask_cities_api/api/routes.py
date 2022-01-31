
from flask import Blueprint, Response, jsonify, request

from .. import db
from ..models import City, Region
from ..schemas import cities_schema, city_schema, region_schema, regions_schema

api = Blueprint('api', __name__)


@api.route('/cities', methods=['GET', 'POST'])
def cities_list():
    """Cities route"""

    if request.method == 'GET':
        all_cities = City.query.all()
        result = cities_schema.dump(all_cities)

        return jsonify(result)

    if request.method == 'POST':
        name = request.json['name']
        region_id = request.json['region_id']

        new_object = City(name, region_id)

        db.session.add(new_object)
        db.session.commit()
        return city_schema.jsonify(new_object)


@api.route('/cities/<int:id>', methods=['GET', 'DELETE', 'PUT'])
def cities_detail(id):
    if request.method == 'GET':
        obj = City.query.get_or_404(id)
        result = city_schema.dump(obj)
        return jsonify(result)


@api.route('/regions', methods=['GET', 'POST'])
def regions_list():
    """Regions route"""

    if request.method == 'GET':
        all_regions = Region.query.all()
        result = regions_schema.dump(all_regions)

        return jsonify(result)

    if request.method == 'POST':
        name = request.json['name']

        new_object = Region(name)

        db.session.add(new_object)
        db.session.commit()
        return region_schema.jsonify(new_object)


@api.route('/regions/<int:id>', methods=['GET', 'DELETE', 'PUT'])
def regions_detail(id):
    if request.method == 'GET':
        obj = Region.query.get_or_404(id)
        result = region_schema.dump(obj)
        return jsonify(result)
