# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models
from django_mysql.models import JSONField

from BestPlaces.models import User
from bpDjango import settings


class Place(models.Model):
    placeid = models.CharField(db_column='placeId', primary_key=True, max_length=28)  # Field name made lowercase.
    additional_information = JSONField(db_column='additionalInformation', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = True
        db_table = 'Place'


class Visit(models.Model):
    visitid = models.AutoField(db_column='visitId', primary_key=True)  # Field name made lowercase.
    user = models.ForeignKey(User, db_column="user", on_delete=models.CASCADE, default="")
    place = models.CharField(db_column="place", max_length=256, null=False, default="")
    visittime = models.DateTimeField(db_column="visitime", null=True)
    notes = models.TextField(blank=True, null=True)
    money = models.DecimalField(db_column="money", max_digits=5, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Visit'

class Userplaceinformation(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, primary_key=True, on_delete=models.CASCADE, default=User)
    place = models.ForeignKey(Place, on_delete=models.CASCADE, default=Place)
    favorite = models.IntegerField(blank=True, null=True)
    reviewtext = models.TextField(db_column='reviewText', blank=True, null=True)  # Field name made lowercase.
    stars = models.IntegerField(blank=True, null=True)
    reviewshowname = models.IntegerField(db_column='reviewShowName', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        unique_together = (('user','place'),)
        db_table = 'UserPlaceInformation'
