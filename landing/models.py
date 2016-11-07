# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import ugettext_lazy as _
from catalog.models import Property, District


class Article(models.Model):
    class Meta:
        verbose_name = _('Статья')
        verbose_name_plural = _('Статьи')

    header = models.CharField(
        verbose_name=_('Заголовок'),
        max_length=50,
        blank=False)
    text = models.TextField(
        verbose_name=_('Текст'),
        max_length=200,
        blank=False
    )
    slug = models.SlugField(
        verbose_name=_('Slug'),
        max_length=20,
        allow_unicode=True,
        blank=False
    )
    date = models.DateTimeField(verbose_name=_('Дата'), auto_now_add=True)
    is_published = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s %s' % (
            self.header,
            self.date,
            self.slug,
            self.is_published
        )


class ChoiceInfo(models.Model):
    class Meta:
        verbose_name = _('Данные о выборе')
        verbose_name_plural = _('Данные о выборах')

    is_accommodation = models.BooleanField(
        verbose_name=_('Интересует ли проживание'),
        default=False
    )
    is_investments = models.BooleanField(
        verbose_name=_('Интересуют ли инвестиции'),
        default=False
    )
    districts = models.ManyToManyField(
        District,
        verbose_name=_('Район'),
        blank=True
    )
    property_type = models.CharField(
        verbose_name=_('Тип недвижимости'),
        max_length=2,
        choices=Property.TYPE,
        blank=False
    )
    update_date = models.DateTimeField(
        verbose_name=_('Время последнего обновления'),
        auto_now=True
    )

    def __unicode__(self):
        return '%s' % self.id


class UserContacts(models.Model):
    class Meta:
        verbose_name = _('Контакты пользователя')
        verbose_name_plural = _('Контакты пользователей')

    name = models.CharField(verbose_name=_('Имя'), max_length=255)
    phone_number = PhoneNumberField(
        verbose_name=_('Номер телефона'),
        unique=True
    )
    email = models.EmailField(verbose_name=_('Email'), blank=False)
    date = models.DateTimeField(verbose_name=_('Дата'), auto_now_add=True)
    from_property = models.ForeignKey(
        Property,
        null=True,
        blank=True,
        verbose_name=_('Недвижимость')
    )
    choice_info = models.OneToOneField(
        ChoiceInfo,
        verbose_name=_('Данные о выборе'),
        null=True,
        blank=True
    )

    def __unicode__(self):
        return '%s %s %s' % (
            self.name,
            self.phone_number,
            self.email,
        )
