from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Country(models.Model):
	"""django-autocomplete-light tutorial"""
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name

class Person(models.Model):
	"""django-autocomplete-light tutorial"""
	first_name = models.CharField(max_length=100)
	birth_country = models.ForeignKey('Country', on_delete=models.CASCADE)
	
	def __str__(self):
		return self.first_name