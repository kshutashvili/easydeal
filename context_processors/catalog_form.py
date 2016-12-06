from catalog.forms import CatalogFilterForm


def catalog_form(request):
    return {
        'filter_form': CatalogFilterForm(request.GET)
    }
