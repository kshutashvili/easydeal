# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-08 14:00
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0011_auto_20161108_1302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='text',
            field=ckeditor.fields.RichTextField(max_length=200, verbose_name='\u0422\u0435\u043a\u0441\u0442'),
        ),
    ]
