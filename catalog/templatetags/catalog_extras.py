# -*- coding: utf-8 -*-

from django import template
from django.template.defaultfilters import floatformat
from config.models import SiteConfiguration

from landing.models import StaticPage


config = SiteConfiguration.get_solo()
register = template.Library()
@register.filter(name='get_price')
def get_price(property, request):
    price = property.price
    if 'currency' in request.session:
        currency = request.session['currency']
        if currency == 'USD':
            result_price = str(floatformat(price * config.usd_rate)) + ' USD'
        elif currency == 'EUR':
            result_price = str(floatformat(price * config.euro_rate)) + ' EURO'
        elif currency == 'RUB':
            result_price = str(floatformat(price * config.rub_rate)) + ' РУБ'
        else:
            result_price = str(floatformat(price)) + ' THB'
    else:
        result_price = str(floatformat(price)) + ' THB'
    return result_price


@register.simple_tag
def get_static_page(slug):
    try:
        static_page = StaticPage.objects.get(slug=slug)
    except StaticPage.DoesNotExist:
        static_page = None
    return static_page
