from django.shortcuts import render
from django.shortcuts import redirect
from django.http import Http404

from config.forms import SelectCurrencyForm


def currency(request):
    if request.method == 'POST':
        select_currency_form = SelectCurrencyForm(request.POST)
        if select_currency_form.is_valid():
            data = select_currency_form.cleaned_data
            request.session['currency'] = data['currency']
        return redirect(request.META.get('HTTP_REFERER'))
    else:
        raise Http404