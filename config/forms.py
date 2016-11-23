from django import forms

from collections import OrderedDict


class SelectCurrencyForm(forms.Form):
    CURRENCIES = (
        ('USD', 'USD'),
        ('RUB', 'RUB'),
        ('EUR', 'EUR'),
        ('THB', 'THB'),
    )
    currency = forms.ChoiceField(
        choices=CURRENCIES,
        label='',
        widget=forms.Select(
            attrs={
                'onchange': 'if(this.value != 0) { this.form.submit(); }'
            }
        ),
    )
