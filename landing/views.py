from django.shortcuts import render

from catalog.forms import CatalogFilterForm, ModalWindowForm


def main(request):
    context = {
        'filter_form': CatalogFilterForm(request.GET),
        'modal_window_form': ModalWindowForm()
    }
    return render(request, 'main.html', context)
