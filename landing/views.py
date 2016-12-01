from django.shortcuts import render

from catalog.forms import CatalogFilterForm


def main(request):
    context = {
        'filter_form': CatalogFilterForm(request.GET)
    }
    return render(request, 'main.html', context)
