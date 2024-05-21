from django.contrib.gis.db import models

class Feature(models.Model):
	name = models.CharField(max_length=232)
	geom = models.GeometryField()
	
	def __str__(self):
		return self.name