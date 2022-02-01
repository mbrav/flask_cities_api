
from flask import Blueprint, Response, current_app, jsonify, request, url_for

from .. import db
from ..models import City, Region
from ..serializers import (cities_serializer, city_serializer,
                           region_serializer, regions_serializer)

auth = Blueprint('auth', __name__)


@auth.route('/cities', methods=['GET'])
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
