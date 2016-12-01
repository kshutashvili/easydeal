from django.shortcuts import render

from catalog.forms import CatalogFilterForm
from catalog.models import District
from catalog.models import Property


def main(request):
    context = {
        'filter_form': CatalogFilterForm(request.GET),
        'property_types': Property.TYPE,
        'districts': District.objects.all()[:12]
    }
    return render(request, 'main.html', context)
