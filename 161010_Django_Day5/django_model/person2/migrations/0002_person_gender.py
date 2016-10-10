# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-07 06:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person2', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='gender',
            field=models.CharField(blank=True, choices=[('m', '남성'), ('f', '여성')], max_length=1),
        ),
    ]