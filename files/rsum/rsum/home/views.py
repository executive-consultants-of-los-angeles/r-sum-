#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Views for the rsum home application."""
import datetime
import json
from collections import OrderedDict

from django.shortcuts import render
from django.db import models
from django.http import HttpResponse
from django.conf import settings

import models
# from export.word import ExportDocument

section = models.section.Section


def index(request):
    """Method for loading the index page.

    :param request: `django.http.HttpRequest` object for index page.
    :type request: object 
    :return: HttpResponse object resulting from execution of render method.
    :rtype: object 
    """

    profile = models.profile.Profile.objects.get(name=settings.OWNER)

    sections = OrderedDict() 
    sections_query = section.objects.values() 
    for section_item in sections_query:
        sections.update({
            section_item.get('name'): json.loads(section_item.get('content'))
        })

    skills = sections.get('skills')

    begin = skills.get('start')
    current_year = float(datetime.date.today().strftime("%Y"))
    career_length = float(current_year) - float(begin)

    for name, skill in skills.items():
        if name != 'start':
            start_skill = float(skill.get('start'))
            years_skill = current_year - start_skill
            experience_value = years_skill / career_length * 100
            experience_string = "{0} year(s)".format(int(years_skill))

            skills.update({
                name: {
                    'name': skills.get(name).get('name'),
                    'start': skills.get(name).get('start'),
                    'experience_value': experience_value,
                    'experience_string': experience_string,
                }
            })
            
            # I don't much like nested for loops, but it's the only way.
            for sub_name, sub_skill in skill.items():
                if (not isinstance(sub_skill, unicode) and
                    not isinstance(sub_skill, int)):
                    start_sub = float(sub_skill.get('start'))
                    years_sub = current_year - start_sub
                    sub_experience_value = years_sub / career_length * 100
                    sub_experience_string = "{0} year(s)".format(int(years_sub))

                    skills.get(name).update({
                        sub_name: {
                            'name': sub_skill.get('name'),
                            'start': sub_skill.get('start'),
                            'experience_value': sub_experience_value,
                            'experience_string': sub_experience_string,
                        }
                    })

    sections.update({'skills':skills})

    context = {
        'profile': profile.name,
        'sections': sections,
    } 
         
    return render(request, 'home/index.html', context)

def export_docx(request, cv_id='1'):
    """Method for exporting Word documents.

    :param request: HttpRequest object for export_docx page.
    :type request: object 
    :return: Word document generated by export module.
    :rtype: object
    stream = ExportDocument().export(cv_id)

    # Special thanks to: https://stackoverflow.com/a/24122313 

    length = stream.tell()
    stream.seek(0)
    response = HttpResponse(
        stream.getvalue(),
        content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document'
    )
    response['Content-Disposition'] = 'attachment; filename={0}-cv.docx'.format(settings.OWNER)
    response['Content-Length'] = length
    return response 

    """
    return render(request, 'home/index.html', {}) 
