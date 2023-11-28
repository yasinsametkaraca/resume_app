from django.shortcuts import render
from feature import models as feature_models


def index(request):

    skills = feature_models.Skill.objects.all()
    skills_mapped = {}
    for elem in skills:
        if elem.skill_type:
            if elem.skill_type.name not in skills_mapped.keys():
                skills_mapped[elem.skill_type.name] = [elem]
            else:
                skills_mapped[elem.skill_type.name].append(elem)

    # experience
    experiences = feature_models.Experience.objects.all()

    context = {
        'skills_mapped': skills_mapped,
        'experiences': experiences,
    }

    return render(request, 'index.html', context=context)

