from modeltranslation.translator import register, TranslationOptions

from .models import District, Property, PropertyQuality


@register(District)
class DistrictTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(Property)
class PropertyTranslationOptions(TranslationOptions):
    fields = (
        'name', 'additional_info'
    )


@register(PropertyQuality)
class PropertyQualityTranslationOptions(TranslationOptions):
    fields = ('name',)
