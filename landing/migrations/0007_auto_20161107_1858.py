# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-07 18:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0006_auto_20161107_1707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choiceinfo',
            name='districts',
            field=models.ManyToManyField(blank=True, to='catalog.District', verbose_name='\u0420\u0430\u0439\u043e\u043d'),
        ),
        migrations.AlterField(
            model_name='usercontacts',
            name='choice_info',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='landing.ChoiceInfo', verbose_name='\u0414\u0430\u043d\u043d\u044b\u0435 \u043e \u0432\u044b\u0431\u043e\u0440\u0435'),
        ),
        migrations.AlterField(
            model_name='usercontacts',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, unique=True, verbose_name='\u041d\u043e\u043c\u0435\u0440 \u0442\u0435\u043b\u0435\u0444\u043e\u043d\u0430'),
        ),
    ]