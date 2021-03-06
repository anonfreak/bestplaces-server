# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-05-01 17:56
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BestPlaces', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visit',
            name='place',
            field=models.ForeignKey(db_column='place', default='', on_delete=django.db.models.deletion.CASCADE, to='BestPlaces.Place'),
        ),
        migrations.AlterField(
            model_name='visit',
            name='user',
            field=models.ForeignKey(db_column='user', default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
