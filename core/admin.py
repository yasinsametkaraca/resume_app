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


