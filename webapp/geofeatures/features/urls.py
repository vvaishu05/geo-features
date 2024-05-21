from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import FeatureViewSet


router = DefaultRouter()  # automatically creates the URL routes for viewsets
router.register(r'features', FeatureViewSet)

urlpatterns = [
	path('', include(router.urls)),
]
