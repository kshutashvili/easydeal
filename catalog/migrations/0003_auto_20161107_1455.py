# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-07 14:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20161106_1229'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='district',
            options={'verbose_name': '\u0420\u0430\u0439\u043e\u043d'},
        ),
        migrations.AlterModelOptions(
            name='property',
            options={'verbose_name': '\u041d\u0435\u0434\u0432\u0438\u0436\u0438\u043c\u043e\u0441\u0442\u044c'},
        ),
        migrations.AlterModelOptions(
            name='propertyphoto',
            options={'verbose_name': '\u0424\u043e\u0442\u043e\u0433\u0440\u0430\u0444\u0438\u044f \u043d\u0435\u0434\u0432\u0438\u0436\u0438\u043c\u043e\u0441\u0442\u0438'},
        ),
    ]