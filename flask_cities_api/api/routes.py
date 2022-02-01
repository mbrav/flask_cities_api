
from flask import (Blueprint, Response, current_app, jsonify,
                   request, url_for)

from .. import db
from ..models import City, Region
from ..serializers import (cities_serializer, city_serializer,
                           region_serializer, regions_serializer)

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
            prev = url_for('api.cities_list', page=page-1)
        next = None
        if pagination.has_next:
            next = url_for('api.cities_list', page=page+1)

        return jsonify({
            'count': pagination.total,
            'next': next,
            'prev': prev,
            'posts': [city_serializer.dump(obj)
                      for obj in objs],
        })

    if request.method == 'POST':

        name = request.json.get('name', None)
        region_id = request.json.get('region_id', None)

        if not name:
            return {"name": "Please provide a city name"}, 400

        if not region_id:
            return {"region_id": "Please provide a region_id"}, 400

        try:
            Region.query.get_or_404(region_id)
        except:
            return {"region_id": "Region with such id does not exist"}, 400

        new_object = City(**request.json)

        db.session.add(new_object)
        db.session.commit()

        result = city_serializer.dump(new_object)
        return jsonify(result)


@api.route('/cities/<int:id>', methods=['GET', 'DELETE', 'PUT'])
def cities_detail(id):
    """Cities detail view"""

    obj = City.query.get_or_404(id)

    if request.method == 'GET':
        result = city_serializer.dump(obj)
        return jsonify(result)

    if request.method == 'PUT':
        region_id = request.json['region_id']

        try:
            Region.query.get_or_404(region_id)
        except:
            return {"region_id": "Region with such id does not exist"}, 400

        obj.name = request.json['name']
        obj.region_id = region_id
        obj.population = request.json['population']
        obj.year_founded = request.json['year_founded']

        db.session.commit()

        result = city_serializer.dump(obj)
        return jsonify(result)

    if request.method == 'DELETE':
        db.session.delete(obj)
        db.session.commit()
        return {"message": "City deleted"}, 204


@api.route('/regions', methods=['GET', 'POST'])
def regions_list():
    """Regions route"""

    if request.method == 'GET':
        page = request.args.get('page', 1, type=int)
        pagination = Region.query.paginate(
            page,
            per_page=current_app.config['FLASK_CITIES_PAGINATION'],
            error_out=False)

        objs = pagination.items
        prev = None
        if pagination.has_prev:
            prev = url_for('api.regions_list', page=page-1)
        next = None
        if pagination.has_next:
            next = url_for('api.regions_list', page=page+1)

        return jsonify({
            'count': pagination.total,
            'next': next,
            'prev': prev,
            'posts': [region_serializer.dump(obj)
                      for obj in objs],
        })

    if request.method == 'POST':
        name = request.json.get('name', None)

        if not name:
            return {"name": "Please provide a region name"}, 400

        new_object = Region(name)

        db.session.add(new_object)
        db.session.commit()

        result = region_serializer.dump(new_object)
        return jsonify(result)


@api.route('/regions/<int:id>', methods=['GET', 'DELETE', 'PUT'])
def regions_detail(id):
    """Region detail view"""

    obj = Region.query.get_or_404(id)

    if request.method == 'GET':
        result = region_serializer.dump(obj)
        return jsonify(result)

    if request.method == 'PUT':

        name = request.json.get('name', None)

        if not name:
            return {"name": "Please provide a region name"}, 400

        obj.name = name
        db.session.commit()

        result = city_serializer.dump(obj)
        return jsonify(result)

    if request.method == 'DELETE':
        db.session.delete(obj)
        db.session.commit()
        return {"message": "Region deleted"}, 204
