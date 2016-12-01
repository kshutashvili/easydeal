# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django import forms
from django.core import validators
from django.utils.translation import ugettext_lazy as _

from catalog.models import Property
from catalog.models import District
from landing.models import ChoiceInfo


class CatalogFilterForm(forms.Form):
    type = forms.ChoiceField(
        choices=Property.TYPE,
        widget=forms.Select(attrs={
            'placeholder': _('Все'),
            'class': 'filter-input',
        }),
        required=False,
    )
    district = forms.ModelChoiceField(
        queryset = District.objects.all(),
        empty_label=None,
        widget=forms.Select(attrs={
            'class': 'filter-input',
        }),
        required=False,
    )
    min_num_bedrooms = forms.IntegerField(
        widget=forms.TextInput(attrs={
            'placeholder': _('От'),
            'class': 'filter-input',
        }),
        required=False,
    )
    max_num_bedrooms = forms.IntegerField(
        widget=forms.TextInput(attrs={
            'placeholder': _('До'),
            'class': 'filter-input',
        }),
        required=False,
    )
    min_price = forms.IntegerField(
        widget=forms.TextInput(attrs={
            'placeholder': _('От'),
            'class': 'filter-input',
        }),
        required=False,
    )
    max_price = forms.IntegerField(
        widget=forms.TextInput(attrs={
            'placeholder': _('До'),
            'class': 'filter-input',
        }),
        required=False,
    )
