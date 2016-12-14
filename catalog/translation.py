from modeltranslation.translator import register, TranslationOptions

from .models import District, Property


@register(District)
class DistrictTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(Property)
class PropertyTranslationOptions(TranslationOptions):
    fields = (
        'property_type', 'name', 'district', 'additional_info'
    )
