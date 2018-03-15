.. rsum documentation master file, created by
   sphinx-quickstart on Sat Jan  6 08:00:05 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to rsum's documentation!
================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   modules/home
   modules/export
   continuous/index

Environment
===========

The software expects two environment variables to be defined for configuration.

RSUM_ENV
--------

This defines the url for the current résumé.  On the Gahan Corp integration system, the resulting output is something like xander.gahan-corporation.com for a value of `xander`.  This also defines where the code will look for static files, so a value of `xander` will cause the software to look for static files under static/profiles/xander from the root directory of the project. 

RSUM_GAID
---------

This sets a Google Analytics ID for tracking information about visitors to the generated websites.


All the Badges
==============

.. image:: https://travis-ci.org/gahan-corporation/rsum.application.svg?branch=master
   :target: https://travis-ci.org/gahan-corporation/rsum.application

.. image:: https://api.codacy.com/project/badge/Coverage/e8ccc643c99147dca4fd98a8b2851451
   :alt: Coverage Badge
   :target: https://www.codacy.com/app/gahancorpcfo/rsum.application?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=gahan-corporation/rsum.application&amp;utm_campaign=Badge_Coverage

.. image:: https://api.codacy.com/project/badge/Grade/e8ccc643c99147dca4fd98a8b2851451
   :alt: Grade Badge
   :target: https://www.codacy.com/app/gahancorpcfo/rsum.application?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=gahan-corporation/rsum.application&amp;utm_campaign=Badge_Grade

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
