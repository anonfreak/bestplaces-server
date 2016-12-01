# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import JSONField
from django.db import models


class Place(models.Model):
    placeid = models.CharField(db_column='placeId', primary_key=True, max_length=28)  # Field name made lowercase.
    additionalInformation = JSONField(db_column='additionalInformation', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'Place'


class User(AbstractUser):
    username = models.CharField(primary_key=True, max_length=45, unique=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    hometown = models.CharField(max_length=45, blank=True, null=True)

    USERNAME_FIELD = "username"


class Visit(models.Model):
    visitid = models.AutoField(db_column='visitId', primary_key=True)  # Field name made lowercase.
    user = models.ForeignKey('User', User.username, db_column='user')
    place = models.ForeignKey('Place', Place.placeid, db_column='place')
    visitime = models.DateTimeField()
    notes = models.TextField(blank=True, null=True)
    money = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Visit'

class Userplaceinformation(models.Model):
    user = models.ForeignKey('User', User.username, db_column='user', primary_key=True)
    place = models.ForeignKey('Place',Place.placeid, db_column='place', primary_key=True)
    favorite = models.IntegerField(blank=True, null=True)
    reviewtext = models.TextField(db_column='reviewText', blank=True, null=True)  # Field name made lowercase.
    stars = models.IntegerField(blank=True, null=True)
    reviewshowname = models.IntegerField(db_column='reviewShowName', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'UserPlaceInformation'
        unique_together = (('user', 'place'),)
