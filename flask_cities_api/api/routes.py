
from flask import Blueprint, Response, current_app, jsonify, request

from .. import db
from ..models import City, Region
from ..serializers import (
    cities_serializer, city_serializer, region_serializer, regions_serializer)

api = Blueprint('api', __name__)


@api.route('/cities', methods=['GET', 'POST'])
def cities_list():
    """Cities route"""

    if request.method == 'GET':
        page = request.args.get('page', 1, type=int)
        pagination = City.query.paginate(
            page,
            per_page=current_app.config['FLASK_CITIES_PAGINATION'],
            error_out=False)

        objs = pagination.items
        prev = None
        if pagination.has_prev:
            prev = url_for('api.cities_list', page=cities-1)
        next = None
        if pagination.has_next:
            next = url_for('api.cities_list', page=cities+1)

        print(objs[0])
        return jsonify({
            'prev': prev,
            'next': next,
            'count': pagination.total,
            'posts': [obj.to_json() for obj in objs],
        })

        all_cities = City.query.all()
        result = cities_serializer.dump(all_cities)

        return jsonify(result)

    if request.method == 'POST':
        name = request.json['name']
        region_id = request.json['region_id']

        new_object = City(name, region_id)

        db.session.add(new_object)
        db.session.commit()
        return city_serializer.jsonify(new_object)


@api.route('/cities/<int:id>', methods=['GET', 'DELETE', 'PUT'])
def cities_detail(id):
    if request.method == 'GET':
        obj = City.query.get_or_404(id)
        result = city_serializer.dump(obj)
        return jsonify(result)


@api.route('/regions', methods=['GET', 'POST'])
def regions_list():
    """Regions route"""

    if request.method == 'GET':
        all_regions = Region.query.all()
        result = regions_serializer.dump(all_regions)

        return jsonify(result)

    if request.method == 'POST':
        name = request.json['name']

        new_object = Region(name)

        db.session.add(new_object)
        db.session.commit()
        return region_serializer.jsonify(new_object)


@api.route('/regions/<int:id>', methods=['GET', 'DELETE', 'PUT'])
def regions_detail(id):
    if request.method == 'GET':
        obj = Region.query.get_or_404(id)
        result = region_serializer.dump(obj)
        return jsonify(result)
