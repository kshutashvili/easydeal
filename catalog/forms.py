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
            'placeholder': _('Мин.'),
            'class': 'filter-input',
        }),
        required=False,
    )
    max_num_bedrooms = forms.IntegerField(
        widget=forms.TextInput(attrs={
            'placeholder': _('Макс.'),
            'class': 'filter-input',
        }),
        required=False,
    )
    min_price = forms.IntegerField(
        widget=forms.TextInput(attrs={
            'placeholder': _('Мин.'),
            'class': 'filter-input',
        }),
        required=False,
    )
    max_price = forms.IntegerField(
        widget=forms.TextInput(attrs={
            'placeholder': _('Макс.'),
            'class': 'filter-input',
        }),
        required=False,
    )


class ModalWindowForm(forms.ModelForm):
    class Meta:
        model = ChoiceInfo
        fields = ('property_type',)
        widgets = {
            'property_type': forms.Select(attrs={
                'class': 'target', 'name': 'type', 'next': 'submit'
            })
        }

    def __init__(self, *args, **kwargs):
        super(ModalWindowForm, self).__init__(*args, **kwargs)
        self.fields['property_type'].empty_label = None
        TYPE_FOR_DISPLAY = (
            ('v', _('Вилла')),
            ('t', _('Таунхаус')),
            ('c', _('Кондоминиум')),
        )
        choices = [
            (value, name)
            for mark, name in TYPE_FOR_DISPLAY
            for key, value in Property.TYPE
            if key == mark
        ]
        self.fields['property_type'].choices = choices
