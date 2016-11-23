from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from .models import Property


class DetailView(TemplateView):
    template_name = 'catalog/product_detail.html'

    def get(self, request, id):
        property = get_object_or_404(Property, pk=id)
        return render(
            request,
            self.template_name,
            {'property': property}
        )
