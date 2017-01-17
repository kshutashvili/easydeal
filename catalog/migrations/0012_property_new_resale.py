# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-15 17:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0011_property_end_building'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='new_resale',
            field=models.CharField(choices=[('n', 'New'), ('r', 'Resale')], default='n', max_length=1, verbose_name='New/Resale'),
        ),
    ]