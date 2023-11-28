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


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['id', 'order', 'name', 'description', 'percentage', 'created_at', 'updated_at']
    list_filter = ['order', 'name', 'description', 'percentage', 'created_at', 'updated_at']
    search_fields = ['name', 'description', 'percentage']
    list_editable = ['order', 'name', 'percentage']

    class Meta:
        model = Skill
