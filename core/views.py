from django.shortcuts import render, get_object_or_404, redirect
from core.models import Document
from core import utils
from feature import models as feature_models


def layout(request):  # burada paylaşılan herşey için context oluşturulur. Bu context her sayfada kullanılır. Bu sayede her sayfada aynı şeyleri tekrar tekrar yazmamız gerekmez. Burada layout fonksiyonu settings içerisindeki TEMPLATES e eklenir.
    site_title = utils.get_general_setting_parameter(setting_name='site_title')  # get site title from database. site_title.parametre = Yasin Samet KARACA
    site_keywords = utils.get_general_setting_parameter(setting_name='site_keywords')  # get site keywords from database. site_keywords.parametre = Yasin Samet KARACA, Yasin Samet, KARACA
    site_description = utils.get_general_setting_parameter(setting_name='site_description')

    # person
    person_name = utils.get_general_setting_parameter(setting_name='person_name')
    person_job = utils.get_general_setting_parameter(setting_name='person_job')
    person_about_me = utils.get_general_setting_parameter(setting_name='person_about_me')
    person_mail = utils.get_general_setting_parameter(setting_name='person_mail')
    person_address = utils.get_general_setting_parameter(setting_name='person_address')
    person_about_myself_welcome = utils.get_general_setting_parameter(setting_name='person_about_myself_welcome')
    person_about_myself_footer = utils.get_general_setting_parameter(setting_name='person_about_myself_footer')

    # images
    header_logo = utils.get_image('header_logo')
    person_image = utils.get_image('person_image')
    site_favicon = utils.get_image('site_favicon')

    # documents
    documents = Document.objects.filter(show_on_page=True)

    # social media
    social_medias = feature_models.SocialMedia.objects.all()

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
        'documents': documents,
        'social_medias': social_medias,
    }
    return context


def redirect_urls(request, slug):
    document = get_object_or_404(Document, slug=slug)
    return redirect(document.file.url)
