# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-10 08:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_auto_20161207_1358'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='hot',
            field=models.BooleanField(default=False, verbose_name='\u0413\u043e\u0440\u044f\u0447\u0435\u0435'),
        ),
    ]