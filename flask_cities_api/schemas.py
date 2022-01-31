from . import ma


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
