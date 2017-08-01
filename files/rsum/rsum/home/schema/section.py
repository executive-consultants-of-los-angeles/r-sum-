#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import print_function

from django.db import models
from home.schema.cv import CV

class Section(models.Model):
    cv = models.ForeignKey(CV, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, default='section')
    value = models.CharField(max_length=200, null=True) 
    iterable = models.BooleanField(default=False)

    def get_sections(self, cv):
        sections = []
        for section in list(
            Section.objects.filter(
                cv = cv
            ).order_by('id').values()
        ):
            if section.get('value') == u"<type 'list'>":
                ss = SubSection( section = self )  
                section.update({
                    'value': ss.get_sub_section(
                        Section.objects.filter(
                            id = section.get('id')
                        )
                    ),
                })
            if section.get('value') == u"<type 'dict'>":
                ss = SubSection( section = self )  
                section.update({
                    'value': ss.get_sub_section(
                        Section.objects.filter(
                            id = section.get('id')
                        )
                    ),
                })
            sections.append(section)
        return sections
    
    def save_section(self, cv, name, section):
        if section == None:
            return None
        s_i = Section()
        s_i.cv = cv
        s_i.name = name 

        if type(section) == type(str()):
            s_i.value = section
            s_i.save()
        else:
            s_i.value = type(section)
            s_i.iterable = True
            s_i.save()
            ss = SubSection()
            ss.save_sub_sections(section, s_i)

        return Section.objects.values_list()
