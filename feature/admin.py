from django.contrib import admin
from feature.models import Skill, SkillTypes, Experience, Education, SocialMedia


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


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['id', 'company_name', 'job_position', 'job_location', 'start_date', 'end_date']
    search_fields = ['company_name', 'job_position', 'job_location', 'start_date', 'end_date']
    list_editable = ['company_name', 'job_position', 'job_location', 'start_date', 'end_date']

    class Meta:
        model = Experience


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['id', 'school_name', 'faculty', 'department', 'start_date', 'end_date']
    search_fields = ['school_name', 'department', 'start_date', 'end_date']
    list_editable = ['school_name', 'faculty', 'department', 'start_date', 'end_date']

    class Meta:
        model = Education


@admin.register(SocialMedia)
class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'url', 'icon']
    search_fields = ['name', 'url', 'icon']
    list_editable = ['name', 'url', 'icon']

    class Meta:
        model = SocialMedia
