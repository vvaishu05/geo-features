from rest_framework_gis.serializers import GeoFeatureModelSerializer
from .models import Feature


class FeatureSerializer(GeoFeatureModelSerializer):
	class Meta:
		model = Feature
		geo_field = "geom"
		fields = ('id', 'name', 'geom')
