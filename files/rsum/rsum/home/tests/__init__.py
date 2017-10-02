#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests for the rsum home application. """
from __future__ import unicode_literals

from django.test import TestCase

import yaml

import home 

from exam.cv import CVTestCase
from exam.cv import CVGetsTestCase
from exam.section import SectionTestCase
from exam.section import GetSectionTestCase
from exam.subsection import SubSectionTestCase
from exam.subsection import GetSubSectionTestCase
from exam.project import ProjectTestCase
from exam.project import GetProjectTestCase
from exam.projectitem import ProjectItemTestCase
from exam.projectitem import GetProjectItemTestCase
from exam.entry import EntryTestCase
from exam.entry import GetEntryTestCase
from exam.entryitem import EntryItemTestCase
from exam.entryitem import GetEntryItemTestCase
from exam.views import ViewsTestCase
import cv
import section
import subsection
import project
import projectitem
import entry
import entryitem
