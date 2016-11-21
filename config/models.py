# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from solo.models import SingletonModel
from django.utils.translation import ugettext_lazy as _
from landing.models import Article


class SiteConfiguration(SingletonModel):
    class Meta:
        verbose_name = _('Конфигурация сайта')

    ru = models.CharField(
        verbose_name=_('Текст на русском'),
        max_length=50
    )
    en = models.CharField(
        verbose_name=_('Текст на английском'),
        max_length=50
    )
    targets_info = models.OneToOneField(
        Article,
        verbose_name=_('О целях покупки'),
        related_name='conf_targets_info',
        null=True,
        blank=True
    )
    districts_info = models.OneToOneField(
        Article,
        verbose_name=_('О районах'),
        related_name='conf_districts_info',
        null=True,
        blank=True
    )
    property_types_info = models.OneToOneField(
        Article,
        verbose_name=_('О типах недвижимости'),
        related_name='conf_property_types_info',
        null=True,
        blank=True
    )
    usd_rate = models.DecimalField(
        verbose_name=_('Курс доллара к бату'),
        max_digits=10,
        decimal_places=2
    )
    euro_rate = models.DecimalField(
        verbose_name=_('Курс евро к бату'),
        max_digits=10,
        decimal_places=2
    )
    rub_rate = models.DecimalField(
        verbose_name=_('Курс рубля к бату'),
        max_digits=10,
        decimal_places=2
    )

    def __unicode__(self):
        return 'Site Configuration'
