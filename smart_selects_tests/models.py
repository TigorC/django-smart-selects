# coding: utf-8
from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from smart_selects.db_fields import ChainedForeignKey


@python_2_unicode_compatible
class Continent(models.Model):
    continent = models.CharField(max_length=45)

    def __str__(self):
        return self.continent


@python_2_unicode_compatible
class Country(models.Model):
    continent = models.ForeignKey(Continent)
    country = models.CharField(max_length=45)

    def __str__(self):
        return self.country


@python_2_unicode_compatible
class Location(models.Model):
    continent = models.ForeignKey(Continent)
    country = ChainedForeignKey(
        Country,
        chained_field="continent",
        chained_model_field="continent",
        show_all=False, auto_choose=True)
    city = models.CharField(max_length=50)
