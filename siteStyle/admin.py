from django.contrib import admin
from siteStyle.models import SiteRichText, SiteString, SiteColor

# Register your models here.
@admin.register(SiteString)
class SiteStringAdmin(admin.ModelAdmin):
    list_display = ['key', 'value']

@admin.register(SiteColor)
class SiteColorAdmin(admin.ModelAdmin):
    list_display = ['name', 'color']

@admin.register(SiteRichText)
class SiteRichTextAdmin(admin.ModelAdmin):
    list_display = ['name', 'value']