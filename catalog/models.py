# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse


def property_directory_path(instance, photo):
    return 'catalog/%s/%s' % (instance.property_id, photo)


class PropertyQuality(models.Model):
    class Meta:
        verbose_name = _('Класс недвижимости')
        verbose_name_plural = _('Классы недвижимости')

    name = models.CharField(
        verbose_name=_('Название'),
        max_length=250
    )

    def __unicode__(self):
        return self.name


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
        ('c', _(u'Кондоминиум')),
        ('t', _(u'Таунхаус')),
        ('v', _(u'Вилла')),
    )
    STATUS = (
        ('n', _(u'New')),
        ('r', _(u'Resale')),
    )
    property_type = models.CharField(
        verbose_name=_('Тип недвижимости'),
        max_length=2,
        choices=TYPE,
        blank=False
    )
    name = models.CharField(verbose_name=_(u'Имя'), max_length=100)
    district = models.ForeignKey(District, null=True, verbose_name=_('Район'))
    quality = models.ForeignKey(PropertyQuality, null=True, blank=True,
                                verbose_name=_('Класс'))
    # means in square meters
    distance_to_beach = models.DecimalField(
        verbose_name=_('Расстояние до пляжа'),
        max_digits=10,
        decimal_places=2
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
        blank=True
    )
    price = models.DecimalField(
        verbose_name=_('Цена'),
        max_digits=10,
        decimal_places=2
    )
    hot = models.BooleanField(
        verbose_name=_('Горячее'),
        default=False
    )
    end_building = models.DateField(
        verbose_name=_('Дата завершения строительства'),
        help_text=_(
            'Имеет значение только месяц и год. День можно указать любой.'
        )
    )
    new_resale = models.CharField(
        verbose_name=_('New/Resale'),
        choices=STATUS,
        max_length=1,
        default='n',
    )

    def __unicode__(self):
        return '%s %s %s %s' % (
            self.name,
            self.property_type,
            self.district,
            self.price
        )

    def get_images(self):
        return PropertyPhoto.objects.filter(property=self)

    def get_title_image(self):
        return self.get_images().first()

    def get_absolute_url(self):
        return reverse('catalog:detail', args=[str(self.id)])
