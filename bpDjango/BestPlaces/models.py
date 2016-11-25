from __future__ import unicode_literals

from django.db import models

class User(models.Model):
    username = models.CharField(max_length=45, primary_key=True)
    email = models.EmailField()
    password = models.CharField(max_length=128)