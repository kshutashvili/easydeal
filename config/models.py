# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from decimal import Decimal

from django.db import models
from solo.models import SingletonModel
from django.utils.translation import ugettext_lazy as _
from landing.models import Article


class SiteConfiguration(SingletonModel):
    class Meta:
        verbose_name = _('Конфигурация сайта')

    header = models.CharField(
        verbose_name=_('Заголовок'),
        max_length=150,
    )
    text = models.TextField(
        verbose_name=_('Текст')
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
        decimal_places=2,
        default=Decimal('0')
    )
    euro_rate = models.DecimalField(
        verbose_name=_('Курс евро к бату'),
        max_digits=10,
        decimal_places=2,
        default=Decimal('0')
    )
    rub_rate = models.DecimalField(
        verbose_name=_('Курс рубля к бату'),
        max_digits=10,
        decimal_places=2,
        default=Decimal('0')
    )

    def __unicode__(self):
        return 'Site Configuration'
