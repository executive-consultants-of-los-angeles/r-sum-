#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Module to define class for SubItem objects."""
from __future__ import unicode_literals
from __future__ import print_function

import json

from django.db import models


class SubItem(models.Model):
    """Class that includes methods related to the SubItem model.

    .. attribute:: sub_section
       
       Associated :obj:`home.models.subsection.SubSection` object.

    .. attribute:: name 

       Name of content to be stored in SubItem.

    .. attribute:: content 

       Content to be stored in SubItem.
    """
    sub_section = models.ForeignKey(
        'home.SubSection',
        on_delete=models.CASCADE
    ) 
    name = models.CharField(max_length=200, null=True)
    content = models.TextField()

    @classmethod
    def create(cls, name='default', *args, **kwargs): 
        """Class method to handle creation of SubItem objects for testing.
        
        :param cls: The SubItem class.
        :type cls: :obj:`home.models.sub_section_item.SubItem`
        :param str name: Name of the sub_section_item.
        :param str content: Content for the sub_section_item.
        :return: Reference to the created Entry.
        :rtype: :obj:`home.models.entry.Entry`
        """
        content = kwargs.get('content')
        print(content)
        sub_section = kwargs.get('sub_section')
        sub_item = cls(name=name, content=content, sub_section=sub_section)
        sub_item.save()



    def get_sub_section_items(self, subsection):
        """Get all SubItem objects.
        
        :param subsection:
            Related :obj:`home.models.subsection.SubSection` object.
        :type subsection: :obj:`home.models.subsection.SubSection`
        :return: List of dictionaries containing stored sub_section_items.
        :rtype: list(dict(str, str))
        """
        #: print(subsection)
        sub_section_items = []
        for sub_section_item in list(
            SubItem.objects.filter(
                sub_section=subsection
            ).order_by('id').values()
        ):
            sub_section_items.append(sub_section_item)
            #: print(json.dumps(sub_section_items,indent=1))
        return sub_section_items

    def save_sub_section_items(self, sub_section_items, sub_section, name):
        """Save all SubItem objects.

        :param sub_section_items: List of SubItem objects to be saved.
        :type sub_section_items: list(str) or dict(str, str)
        :param sub_section: 
            Related :obj:`home.models.subsection.SubSection` object.
        :type sub_section: :obj:`home.models.subsection.SubSection`
        :param name: Name of SubItem content.
        :type name: str
        :return: Dictionary of saved SubItem values.
        :rtype: dict(str, str)
        """
        # print(json.dumps(sub_section_items, indent=1))
        # print(name)
        if name == 'id':
            return None

        if isinstance(sub_section_items, dict):
            for k, v in sub_section_items.iteritems():
                p_i = SubItem()
                p_i.sub_section = sub_section
                p_i.name = k
                p_i.content = v
                p_i.save()
            return SubItem.objects.values()

        if isinstance(sub_section_items, list):
            for k, v in enumerate(sub_section_items):
                p_i = SubItem()
                p_i.sub_section = sub_section
                p_i.name = name
                p_i.content = type(v)
                p_i.save()
                pi = SubItemItem()
                pi.save_sub_section_item_item(v, p_i)
            return SubItem.objects.values()

        if (
            isinstance(sub_section_items, str) or
            isinstance(sub_section_items, unicode)
        ):
            p_i = SubItem()
            p_i.sub_section = sub_section
            p_i.name = getattr(sub_section, 'name') 
            p_i.content = sub_section_items
            p_i.save()
            return SubItem.objects.values()

    class Meta:
        app_label = "home"
        managed = True
