# -*- coding: utf-8 -*-

from django.contrib import admin
from .models import Article, UserContacts, ChoiceInfo


class UserContactsAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'phone_number',
        'email',
        'date'
    )


class ChoiceInfoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'update_date',
        'is_accommodation',
        'is_investments',
        'get_districts',
        'property_type'
    )
    list_filter = ['property_type']

    def get_districts(self, obj):
        """
        Display of object's districts as string

        if string's len >= DISPLAY_WIDTH
            it replace last letters of string on STR_END
        """
        DISPLAY_WIDTH = 25
        STR_END = '...'
        districts = sorted([str(i) for i in obj.districts.all()])
        result = ', '.join(districts)
        if len(result) <= DISPLAY_WIDTH:
            return result
        else:
            return result[:DISPLAY_WIDTH - len(STR_END)] + STR_END

    get_districts.short_description = ('Районы')


admin.site.register(Article)
admin.site.register(ChoiceInfo, ChoiceInfoAdmin)
admin.site.register(UserContacts, UserContactsAdmin)
