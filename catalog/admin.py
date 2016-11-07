from django.contrib import admin
from .models import District, Property, PropertyPhoto


class PropertyPhotoInline(admin.TabularInline):
    model = PropertyPhoto
    extra = 1


class PropertyAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'property_type',
        'district',
        'distance_to_beach',
        'space',
        'number_of_bedrooms',
        'price'
    )
    list_filter = ['property_type']
    inlines = [PropertyPhotoInline]


admin.site.register(District)
admin.site.register(Property, PropertyAdmin)
