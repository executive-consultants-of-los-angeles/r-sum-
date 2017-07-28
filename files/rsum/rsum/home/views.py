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
    for i in range(1,len(models.Section.objects.all())+1):
        sections.append(
            models.Section.objects.filter(id=i).values()[0]
        )


    for i in range(0,len(sections)):
        print(sections[i])
        try: 
            subsection = models.SubSection.objects.filter(
                section = sections[i].get('id')
            ).values()[0] 
            sections[i].update({'subsection': subsection})
        except:
            pass
        print(sections)

    context = {
        'sections': models.Section.objects.all().__dict__,
        'sub_sections': models.SubSection.objects.all().__dict__,
    }

    return render(request, 'home/index.html', {})
