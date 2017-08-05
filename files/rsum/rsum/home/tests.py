#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

import home
import yaml
from exam.cv import CVTestCase
from exam.cv import CVGetsTestCase
from exam.section import SectionTestCase
from exam.subsection import SubSectionTestCase
from exam.project import ProjectTestCase
from exam.project import GetProjectTestCase
from exam.projectitem import ProjectItemTestCase
from exam.projectitem import GetProjectItemTestCase
from exam.entry import EntryTestCase
from exam.entry import GetEntryTestCase
from exam.entryitem import EntryItemTestCase
from exam.entryitem import GetEntryItemTestCase
from exam.views import ViewsTestCase
