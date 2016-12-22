# -*- coding: utf-8 -*-

from django import template
from django.template.defaultfilters import floatformat
from config.models import SiteConfiguration

from landing.models import StaticPage
from catalog.utils import get_price_currency


config = SiteConfiguration.get_solo()
register = template.Library()


@register.filter(name='get_price')
def get_price(property, request):
    price = property.price
    if 'currency' in request.session:
        currency = request.session['currency']
        result_price = '{} {}'.format(
            str(floatformat(get_price_currency(price, currency))),
            currency,
        )
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
