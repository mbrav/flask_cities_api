from marshmallow import Schema, fields


class CitySerializer(Schema):
    """City schema"""

    class Meta:
        ordered = True
        fields = ('id', 'name', 'region_id', 'population', 'year_founded')


class RegionSerializer(Schema):
    """Region schema"""

    cities = fields.List(fields.Nested(
        CitySerializer(exclude=('id', 'region_id',))))

    class Meta:
        ordered = True
        fields = ('id', 'name', 'cities')


city_serializer = CitySerializer()
cities_serializer = CitySerializer(many=True)
region_serializer = RegionSerializer()
regions_serializer = RegionSerializer(many=True)
