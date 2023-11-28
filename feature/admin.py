from django.contrib import admin
from feature.models import Skill, SkillTypes


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['id', 'order', 'name', 'description', 'percentage', 'skill_type', 'created_at', 'updated_at']
    list_filter = ['order', 'name', 'description', 'percentage', 'skill_type', 'created_at', 'updated_at']
    search_fields = ['order', 'name', 'description', 'percentage', 'skill_type']
    list_editable = ['order', 'name', 'description', 'percentage', 'skill_type']

    class Meta:
        model = Skill


@admin.register(SkillTypes)
class SkillTypesAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name', ]
    list_editable = ['name', ]

    class Meta:
        model = SkillTypes
