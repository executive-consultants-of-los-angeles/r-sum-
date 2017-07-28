#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import print_function

from django.shortcuts import render
from django.forms.models import model_to_dict

import models

# Create your views here.

def index(request):
    sections = []
    
    cv_i = models.CV()
    cv_i.check_sections()
    for i in range(1,len(models.CV.objects.all())+1):
        sections.append(
            models.Section.objects.filter(id=i).values()[0]
        )


    for k,i in enumerate(sections):
        subsection = models.SubSection.objects.filter(section_id=i.get('id')).values()[0]     
        sections[k].update({'subsection': subsection})
        print(sections)

    context = {
        'sections': models.Section.objects.all().__dict__,
        'sub_sections': models.SubSection.objects.all().__dict__,
        'projects': models.Projects.objects.all().__dict__,
        'project_items_list': models.ProjectItemsList.objects.all().__dict__,
    }

    return render(request, 'home/index.html', {})
