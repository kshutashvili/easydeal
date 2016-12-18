from modeltranslation.translator import register, TranslationOptions

from .models import Article, StaticPage


@register(Article)
class ArticleTranslationOptions(TranslationOptions):
    fields = ('header', 'text')


@register(StaticPage)
class StaticPageTranslationOptions(TranslationOptions):
    fields = ('title', 'content')
