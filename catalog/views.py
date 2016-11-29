from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.exceptions import ObjectDoesNotExist

from catalog.models import Property
from catalog.forms import CatalogFilterForm
from landing.forms import UserContactsForm
from landing.models import UserContacts, ChoiceInfo


class DetailView(TemplateView):
    template_name = 'product_detail.html'

    def get(self, request, id):
        property = get_object_or_404(Property, pk=id)
        contact_form = UserContactsForm()
        return render(
            request,
            self.template_name,
            {
                'property': property,
                'contact_form': contact_form
            }
        )

    def post(self, request, id):
        property = get_object_or_404(Property, pk=id)
        form = UserContactsForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            phone_number = form.cleaned_data.get('phone_number')
            email = form.cleaned_data.get('email')
            user_contacts = UserContacts(
                name=name,
                phone_number=phone_number,
                email=email,
            )
            choice_info_sk = request.session.get('choice_info')
            if choice_info_sk:
                try:
                    choice_info = ChoiceInfo.objects.get(session_key=choice_info_sk)
                    user_contacts.session_key = choice_info
                except ObjectDoesNotExist:
                    pass
            user_contacts.save()
            return redirect('catalog:catalog')
        return redirect(property)


def catalog(request):
    filter_form = CatalogFilterForm(request.GET)
    params = {}
    if filter_form.is_valid():
        if 'type' in request.GET:
            params['property_type'] = request.GET['type']
        if 'district' in request.GET:
            params['district'] = request.GET['district']
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
    contact_form = UserContactsForm()
    try:
        properties = paginator.page(page)
    except PageNotAnInteger:
        properties = paginator.page(1)
    except EmptyPage:
        properties = paginator.page(paginator.num_pages)

    context = {
        'property_list': property_list,
        'properties': properties,
        'filter_form': filter_form,
        'contact_form': contact_form,
    }

    return render(request, 'catalog.html', context)
