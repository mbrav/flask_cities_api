from flask_marshmallow import Marshmallow

from . import app

ma = Marshmallow(app)


class RegionSchema(ma.Schema):
    """Region schema"""

    class Meta:
        fields = ('id', 'name')


class CitySchema(ma.Schema):
    """City schema"""

    class Meta:
        fields = ('id', 'name', 'region_id')


city_schema = CitySchema()
cities_schema = CitySchema(many=True)
region_schema = RegionSchema()
regions_schema = RegionSchema(many=True)
