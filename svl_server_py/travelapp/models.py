from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Country(models.Model):
  nameCountry = models.CharField(max_length=100)
  flagCountry = models.CharField(max_length=50)
  imgCountry = models.CharField(max_length=50)
  slugCountry = models.SlugField(max_length=100)

  def __unicode__(self):
    return self.nameCountry


class Place(models.Model):
  country = models.ForeignKey(Country)
  namePlace = models.CharField(max_length=100)
  latPlace = models.CharField(max_length=100)
  longPlace = models.CharField(max_length=100)
  slugPlace = models.SlugField(max_length=100)

  def __unicode__(self):
    return self.namePlace


class Picture(models.Model):
  country = models.ForeignKey(Country)
  place = models.ForeignKey(Place)
  year = models.CharField(max_length=5)
  month = models.CharField(max_length=20)
  nameImage = models.CharField(max_length=100) 
  legendImage = models.TextField(blank=True) 

  def __unicode__(self):
    return self.namePlace
