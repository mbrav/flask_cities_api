from . import ma


class RegionSerializer(ma.Schema):
    """Region schema"""

    class Meta:
        fields = ('id', 'name')


class CitySerializer(ma.Schema):
    """City schema"""

    class Meta:
        fields = ('id', 'name', 'region_id', 'population', 'year_founded')


city_serializer = CitySerializer()
cities_serializer = CitySerializer(many=True)
region_serializer = RegionSerializer()
regions_serializer = RegionSerializer(many=True)
