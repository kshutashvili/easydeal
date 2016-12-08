from django.shortcuts import render
from django.shortcuts import get_object_or_404

from catalog.forms import CatalogFilterForm
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
