from django.shortcuts import render, get_object_or_404
from core.models import GeneralSetting, ImageSetting
from feature import models as feature_models


def index(request):
    site_title = GeneralSetting.objects.get(name='site_title').parameters  # get site title from database. site_title.parametre = Yasin Samet KARACA
    site_keywords = GeneralSetting.objects.get(name='site_keywords').parameters  # get site keywords from database. site_keywords.parametre = Yasin Samet KARACA, Yasin Samet, KARACA
    site_description = get_object_or_404(GeneralSetting, name='site_description').parameters
    person_name = get_object_or_404(GeneralSetting, name='person_name').parameters
    person_job = get_object_or_404(GeneralSetting, name='person_job').parameters
    person_about_me = get_object_or_404(GeneralSetting, name='person_about_me').parameters
    person_mail = get_object_or_404(GeneralSetting, name='person_mail').parameters
    person_address = get_object_or_404(GeneralSetting, name='person_address').parameters
    person_about_myself_welcome = get_object_or_404(GeneralSetting, name='person_about_myself_welcome').parameters
    person_about_myself_footer = get_object_or_404(GeneralSetting, name='person_about_myself_footer').parameters

    # images
    header_logo = ImageSetting.objects.get(name='header_logo').file.url
    person_image = ImageSetting.objects.get(name='person_image').file.url
    site_favicon = ImageSetting.objects.get(name='site_favicon').file.url

    # skills
    skills = feature_models.Skill.objects.all()
    skills_mapped = {}
    for elem in skills:
        if elem.skill_type:
            if elem.skill_type.name not in skills_mapped.keys():
                skills_mapped[elem.skill_type.name] = [elem]
            else:
                skills_mapped[elem.skill_type.name].append(elem)

    context = {
        'site_title': site_title,
        'site_keywords': site_keywords,
        'site_description': site_description,
        'person_name': person_name,
        'person_job': person_job,
        'person_about_me': person_about_me,
        'person_mail': person_mail,
        'person_address': person_address,
        'person_about_myself_welcome': person_about_myself_welcome,
        'person_about_myself_footer': person_about_myself_footer,
        'header_logo': header_logo,
        'person_image': person_image,
        'site_favicon': site_favicon,
        'skills_mapped': skills_mapped,
    }

    return render(request, 'index.html', context=context)

