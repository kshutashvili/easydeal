from django.contrib import admin

from solo.admin import SingletonModelAdmin
from modeltranslation.admin import TabbedTranslationAdmin

from .models import SiteConfiguration


class SiteConfigurationAdmin(SingletonModelAdmin, TabbedTranslationAdmin):
    pass


admin.site.register(SiteConfiguration, SiteConfigurationAdmin)
