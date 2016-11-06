from django.contrib import admin
from .models import District, Property, PropertyPhoto


class PropertyPhotoLine(admin.TabularInline):
    model = PropertyPhoto
    extra = 1


class DistrictAdmin(admin.ModelAdmin):
    list_display = ('name', )


class PropertyAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'property_type',
        'district',
        'distance_to_beach',
        'space',
        'number_of_bedrooms',
        #'additional_info',
        'price'
    )
    list_filter = ['property_type']
    inlines = [PropertyPhotoLine]


admin.site.register(District, DistrictAdmin)
admin.site.register(Property, PropertyAdmin)
