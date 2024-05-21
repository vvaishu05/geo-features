from django.contrib import admin
from .models import Feature


@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'geom',)
	list_filter = ('name',)
	search_fields = ('name',)
	ordering = ('name',)
