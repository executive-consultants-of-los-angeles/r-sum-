#!/usr/bin/env python
# pylint: disable=no-member
# -*- coding: utf-8 -*-
"""Views for the rsum home application."""
import json
from collections import OrderedDict

from django.shortcuts import render
from django.conf import settings

from home.models.section import Section
from home.models.profile import Profile
from home.models.skills import Skills


def index(request):
    """Load the index page of the rsum application.

    :param request: `django.http.HttpRequest` object for index page.
    :type request: object
    :return: HttpResponse object resulting from execution of render method.
    :rtype: object
    """
    profile = Profile.objects.all()[0]

    sections = OrderedDict()
    sections_query = Section.objects.values()
    for section_item in sections_query:
        sections.update({
            section_item.get('name'): json.loads(section_item.get('content'))
        })

    skills = sections.get('skills')
    skills_obj = Skills(skills)

    sections.update({'skills': skills_obj.calculate_skills(skills)})

    context = {
        'profile': profile,
        'sections': sections,
        'dir': settings.DIR,
    }

    return render(request, 'home/index.html', context)
