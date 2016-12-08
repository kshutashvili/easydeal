from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from catalog.models import Property
from catalog.forms import CatalogFilterForm


class PropertyDetailView(DetailView):
    template_name = 'product_detail.html'
    model = Property
    pk_url_kwarg = 'id'

    def get_context_data(self, **kwargs):
        context = super(PropertyDetailView, self).get_context_data(**kwargs)
        context['filter_form'] = CatalogFilterForm(self.request.GET)
        return context


def catalog(request):
    filter_form = CatalogFilterForm(request.GET)
    params = {}
    if filter_form.is_valid():
        if 'type' in request.GET:
            params['property_type'] = request.GET['type']
        if 'district' in request.GET:
            params['district__id__in'] = request.GET.getlist(u'district')
        if 'min_num_bedrooms' in request.GET and request.GET['min_num_bedrooms']:
            params['number_of_bedrooms__gte'] = request.GET['min_num_bedrooms']
        if 'max_num_bedrooms' in request.GET and request.GET['max_num_bedrooms']:
            params['number_of_bedrooms__lte'] = request.GET['max_num_bedrooms']
        if 'min_price' in request.GET and request.GET['min_price']:
            params['price__gte'] = request.GET['min_price']
        if 'max_price' in request.GET and request.GET['max_price']:
            params['price__lte'] = request.GET['max_price']

    property_list = Property.objects.filter(**params)

    paginator = Paginator(property_list, 10)
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
        'filter_form': filter_form
    }

    return render(request, 'catalog.html', context)
