from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from catalog.models import Property


def main(request):
    return render(request, 'main.html')

def catalog(request):
    property_list = Property.objects.all()

    paginator = Paginator(property_list, 1)
    page = request.GET.get('page')
    try:
        properties = paginator.page(page)
    except PageNotAnInteger:
        properties = paginator.page(1)
    except EmptyPage:
        properties = paginator.page(paginator.num_pages)

    context = {
        'property_list': property_list,
        'properties': properties,
    }

    return render(request, 'catalog.html', context)