from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from config.models import SiteConfiguration
from catalog.models import Property
from catalog.forms import CatalogFilterForm
from catalog.utils import get_price_thb


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
        if request.GET.get('min_num_bedrooms', None):
            params['number_of_bedrooms__gte'] = request.GET['min_num_bedrooms']
        if request.GET.get('max_num_bedrooms', None):
            params['number_of_bedrooms__lte'] = request.GET['max_num_bedrooms']
        if 'currency' in request.session:
            currency = request.session['currency']
            if 'min_price' in request.GET and request.GET['min_price']:
                params['price__gte'] = get_price_thb(
                    request.GET['min_price'], currency)
            if 'max_price' in request.GET and request.GET['max_price']:
                params['price__lte'] = get_price_thb(
                    request.GET['max_price'], currency)

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


class HotView(ListView):
    template_name = 'catalog.html'
    model = Property

    def get_context_data(self, **kwargs):
        context = super(HotView, self).get_context_data(**kwargs)
        context['properties'] = Property.objects.filter(hot=True).order_by('price')
        return context
