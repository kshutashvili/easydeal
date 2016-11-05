from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _


class State(models.Model):
    name = models.CharField(
        verbose_name=_('State'),
        max_length=250
    )

    def __unicode__(self):
        return self.name


class Property(models.Model):
    TYPE = (
        ('c', 'condominium'),
        ('t', 'townhouse'),
        ('v', 'villa'),
    )
    property_type = models.CharField(
        verbose_name=_('Property type'),
        max_length=2,
        choices=TYPE,
        blank=False
    )
    name = models.CharField(verbose_name=_('Name'), max_length=100)
    state = models.ForeignKey(State)
    # means in square meters
    distance_to_beach = models.PositiveIntegerField(
        verbose_name=_('Distance to the beach')
    )
    living_space = models.PositiveIntegerField(
        verbose_name=_('Living space')
    )
    number_of_bedrooms = models.PositiveIntegerField(
        verbose_name=_('Number of bedrooms')
    )
    # information about additional facilities
    additional_info = models.TextField(
        verbose_name=_('Information about additional facilities'),
        max_length=200,
        blank=True
    )
    price = models.FloatField(
        verbose_name=_('Price')
    )
    photo = models.ImageField(
        verbose_name=_('Photo'),
        upload_to='catalog/'
    )
