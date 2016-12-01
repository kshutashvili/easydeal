from django.http.request import HttpRequest
from catalog.models import Property
from catalog.models import District


def modal_window(HttpRequest):
    return {
        'property_types': Property.TYPE,
        'districts': District.objects.all()[:12]
    }
