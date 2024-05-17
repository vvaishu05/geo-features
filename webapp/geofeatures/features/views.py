# Viewsets are a type of class-based view that provides actions. Pagination helps in dividing large sets of data into smaller chunks.
from rest_framework import viewsets, pagination

# Used to filter features that fall within a certain geographical area.
from rest_framework_gis.filters import InBBoxFilter

# Permission class that restricts access to authenticated users only.
from rest_framework.permissions import IsAuthenticated

# Imports the Feature model from the current app’s models.
from .models import Feature

# Serializer to convert Feature instances to JSON and vice versa.
from .serializers import FeatureSerializer


class FeaturePagination(pagination.PageNumberPagination):
	"""Defines a custom pagination class"""

	# Items per page
	page_size = 100


class FeatureViewSet(viewsets.ModelViewSet):
	"""Defines a viewset for the Feature model which automatically provides CRUD operations"""
	
	# only authenticated users that are logged in can access this viewset
	permission_classes = (IsAuthenticated,)
	# Query all instances from Feature model
	queryset = Feature.objects.all()
	# serializer to be used for converting Feature instances to JSON and vice versa
	serializer_class = FeatureSerializer
	# paginate the queryset
	pagination_class = FeaturePagination
	# filter features by geographical bounding box
	filter_backends = (InBBoxFilter,)
	# model field to be used for bounding box filtering
	bbox_filter_field = 'geom'
	# include features that overlap the bounding box edges
	bbox_filter_include_overlapping = True
