#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import print_function

from django.shortcuts import render

import json
import models

# Create your views here.

def index(request):
    sections = []
    
    cv_i = models.CV()
    cv_i.check_sections()
    for i in range(1,len(models.Section.objects.all())+1):
        s = models.Section()
        sections.append(
            s.get_section(i)
        )


    for i in range(0,len(sections)):
        ss = models.SubSection()
        subsections = list(ss.get_sub_section(sections[i].get('id')))
        if len(subsections) > 0:
            sections[i].update({'subsections': subsections})
        print(sections)
        

    context = {
        'sections': models.Section.objects.all().__dict__,
        'sub_sections': models.SubSection.objects.all().__dict__,
    }

    return render(request, 'home/index.html', {})
