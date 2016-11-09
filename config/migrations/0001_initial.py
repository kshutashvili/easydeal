# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-08 19:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SiteConfiguration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ru', models.CharField(max_length=50, verbose_name='\u0422\u0435\u043a\u0441\u0442 \u043d\u0430 \u0440\u0443\u0441\u0441\u043a\u043e\u043c')),
                ('en', models.CharField(max_length=50, verbose_name='\u0422\u0435\u043a\u0441\u0442 \u043d\u0430 \u0430\u043d\u0433\u043b\u0438\u0439\u0441\u043a\u043e\u043c')),
                ('targets', models.URLField(max_length=100, verbose_name='\u041e \u0446\u0435\u043b\u044f\u0445 \u043f\u043e\u043a\u0443\u043f\u043a\u0438')),
                ('districts', models.URLField(max_length=100, verbose_name='\u041e \u0440\u0430\u0439\u043e\u043d\u0430\u0445')),
                ('property_types', models.URLField(max_length=100, verbose_name='\u041e \u0442\u0438\u043f\u0430\u0445 \u043d\u0435\u0434\u0432\u0438\u0436\u0438\u043c\u043e\u0441\u0442\u0438')),
            ],
            options={
                'verbose_name': '\u041a\u043e\u043d\u0444\u0438\u0433\u0443\u0440\u0430\u0446\u0438\u044f \u0441\u0430\u0439\u0442\u0430',
            },
        ),
    ]
