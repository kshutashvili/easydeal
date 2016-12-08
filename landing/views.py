from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.views.generic import View
from django.core.exceptions import ObjectDoesNotExist

from catalog.forms import CatalogFilterForm
from .forms import UserContactsForm
from .models import UserContacts, ChoiceInfo
from landing.models import StaticPage
from landing.models import Article


def main(request):
    context = {
        'filter_form': CatalogFilterForm(request.GET)
    }
    return render(request, 'main.html', context)


def static_page(request, slug):
    page = get_object_or_404(StaticPage, slug=slug)
    context = {
        'page': page,
    }
    return render(request, 'landing/static_page.html', context)


def article(request, slug):
    article = get_object_or_404(Article, slug=slug, is_published=True)
    context = {
        'article': article,
    }
    return render(request, 'landing/article.html', context)


class UserContactsView(View):
    def post(self, request, *args, **kwargs):
        form = UserContactsForm(request.POST)
        if form.is_valid():
            user_contacts = form.save(commit=False)
            choice_info_sk = request.session.get('choice_info')
            if choice_info_sk:
                try:
                    choice_info = ChoiceInfo.objects.get(session_key=choice_info_sk)
                    user_contacts.session_key = choice_info
                except ObjectDoesNotExist:
                    pass
            user_contacts.save()
        return redirect(request.META.get('HTTP_REFERER', '/'))
