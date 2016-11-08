# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-07 17:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_auto_20161107_1644'),
        ('landing', '0005_auto_20161107_1701'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choiceinfo',
            name='district',
        ),
        migrations.AddField(
            model_name='choiceinfo',
            name='districts',
            field=models.ManyToManyField(blank=True, null=True, to='catalog.District', verbose_name='\u0420\u0430\u0439\u043e\u043d'),
        ),
    ]