# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-11 06:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0004_phototag_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='tags',
            field=models.ManyToManyField(blank=True, to='photo.PhotoTag'),
        ),
    ]
