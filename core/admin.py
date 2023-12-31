from django.contrib import admin
from core.models import *


@admin.register(GeneralSetting)
class GeneralSettingAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'parameters', 'created_at', 'updated_at']
    list_filter = ['id', 'name', 'description', 'parameters', 'created_at', 'updated_at']
    search_fields = ['id', 'name', 'description', 'parameters']
    list_editable = ['description', 'parameters']

    class Meta:
        model = GeneralSetting


@admin.register(ImageSetting)
class ImageSettingAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'file', 'created_at', 'updated_at']
    list_filter = ['name', 'description', 'file', 'created_at', 'updated_at']
    search_fields = ['name', 'description', 'file']
    list_editable = ['name', 'description', 'file']

    class Meta:
        model = ImageSetting


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ['id', 'slug', 'file', 'button_text', 'created_at', 'updated_at']
    list_filter = ['slug', 'file', 'button_text', 'created_at', 'updated_at']
    search_fields = ['slug', 'file', 'button_text']
    list_editable = ['slug', 'file', 'button_text']

    class Meta:
        model = Document