from django.contrib import admin
from .models import State, Property


class PropertyAdmin(admin.ModelAdmin):
    list_display = (
        'property_type',
        'name',
        'state',
        'distance_to_beach',
        'living_space',
        'number_of_bedrooms',
        'additional_info',
        'price'
    )


admin.site.register(State)
admin.site.register(Property, PropertyAdmin)
