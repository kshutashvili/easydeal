# -*- coding: utf-8 -*-

from django import forms
from django.utils.translation import ugettext_lazy as _
from phonenumber_field.widgets import PhoneNumberInternationalFallbackWidget

from .models import UserContacts


class UserContactsForm(forms.ModelForm):
    class Meta:
        model = UserContacts
        fields = ('name', 'phone_number', 'email')
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': _(u'имя')}),
            'phone_number': PhoneNumberInternationalFallbackWidget(
                attrs={'placeholder': _(u'телефон')}),
            'email': forms.EmailInput(attrs={'placeholder': _(u'e-mail')}),
        }
