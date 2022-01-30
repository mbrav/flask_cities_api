from flask import Response, jsonify, request

from . import app
from .models import City, Region
from .schemas import cities_schema, city_schema, region_schema, regions_schema


@app.route('/cities', methods=['GET', 'POST'])
def cities():
    """Cities route"""

    if request.method == 'GET':
        all_cities = City.query.all()
        result = cities_schema.dump(all_cities)

        return jsonify({'cities': result})

    if request.method == 'POST':
        name = request.json['name']
        region_id = request.json['region_id']

        new_object = City(name, region_id)

        db.session.add(new_object)
        db.session.commit()
        return city_schema.jsonify(new_object)


@app.route('/regions', methods=['GET', 'POST'])
def regions():
    """Regions route"""

    if request.method == 'GET':
        all_regions = Region.query.all()
        result = regions_schema.dump(all_regions)

        return jsonify({'regions': result})

    if request.method == 'POST':
        name = request.json['name']

        new_object = Region(name)

        db.session.add(new_object)
        db.session.commit()
        return region_schema.jsonify(new_object)


if __name__ == '__main__':
    app.run(debug=True)
