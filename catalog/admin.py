from django.contrib import admin

from modeltranslation.admin import TabbedTranslationAdmin

from .models import District, Property, PropertyPhoto, PropertyQuality


class PropertyPhotoInline(admin.TabularInline):
    model = PropertyPhoto
    extra = 1


class PropertyAdmin(TabbedTranslationAdmin):
    list_display = (
        'name',
        'property_type',
        'district',
        'distance_to_beach',
        'space',
        'number_of_bedrooms',
        'price',
        'hot'
    )
    list_filter = ['property_type']
    inlines = [PropertyPhotoInline]


class DistrictAdmin(TabbedTranslationAdmin):
    pass


class PropertyQualityAdmin(TabbedTranslationAdmin):
    pass


admin.site.register(PropertyQuality, PropertyQualityAdmin)
admin.site.register(District, DistrictAdmin)
admin.site.register(Property, PropertyAdmin)
