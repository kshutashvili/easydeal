from django.http.request import HttpRequest
from catalog.models import Property
from catalog.models import District
from config.models import SiteConfiguration


config = SiteConfiguration.get_solo()
def modal_window(HttpRequest):
    return {
        'property_types': Property.TYPE,
        'districts': District.objects.all()[:12],
        'targets_info': config.targets_info,
        'districts_info': config.districts_info,
        'property_types_info': config.property_types_info,
    }
