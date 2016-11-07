# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _


def property_directory_path(instance, photo):
    return 'catalog/%s/%s' % (instance.property_id, photo)


class District(models.Model):
    class Meta:
        verbose_name = _('Район')
        verbose_name_plural = _('Районы')

    name = models.CharField(
        verbose_name=_('Район'),
        max_length=250
    )

    def __unicode__(self):
        return self.name


class PropertyPhoto(models.Model):
    class Meta:
        verbose_name = _('Фотография недвижимости')
        verbose_name_plural = _('Фотографии недвижимости')

    property = models.ForeignKey('Property')
    image = models.ImageField(
        verbose_name=_('Фото'),
        upload_to=property_directory_path
    )

    def __unicode__(self):
        return '%s %s' % (self.property, self.image)


class Property(models.Model):
    class Meta:
        verbose_name = _('Недвижимость')
        verbose_name_plural = _('Недвижимость')

    TYPE = (
        ('c', 'condominium'),
        ('t', 'townhouse'),
        ('v', 'villa'),
    )
    property_type = models.CharField(
        verbose_name=_('Тип недвижимости'),
        max_length=2,
        choices=TYPE,
        blank=False
    )
    name = models.CharField(verbose_name=_(u'Имя'), max_length=100)
    district = models.ForeignKey(District, null=True, verbose_name=_('Район'))
    # means in square meters
    distance_to_beach = models.PositiveIntegerField(
        verbose_name=_('Расстояние до пляжа')
    )
    space = models.PositiveIntegerField(
        verbose_name=_('Площадь'),
        default=0
    )
    number_of_bedrooms = models.PositiveIntegerField(
        verbose_name=_('Количество спален')
    )
    # information about additional facilities
    additional_info = models.TextField(
        verbose_name=_('Информация о дополнительных сооружениях'),
        max_length=200,
        blank=True
    )
    price = models.DecimalField(
        verbose_name=_('Цена'),
        max_digits=10,
        decimal_places=2
    )

    def __unicode__(self):
        return '%s %s %s %s' % (
            self.name,
            self.property_type,
            self.district,
            self.price
        )