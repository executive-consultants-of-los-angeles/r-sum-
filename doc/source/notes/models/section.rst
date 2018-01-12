home app section model
======================

Here will be a brief but complet e discussion of the properties and attributes of the section model.

Just what is a section anyway?
------------------------------

In this context a section is the first level of categorization applied to a person's c.v.  That is to say, there is the c.v. as a holistic entity, then that is (generally) broken up into constituent parts in order to tell a story that presents the most appealing version of the subject as possible. 

There are further divisions of the data in a c.v., but implementing them in a relational database is clumsy and awkward.  Or at least the author isn't smart enough to make it not clumsy and awkward.  For the sake of this software, there will be only the two layers: the document itself and its sections. 

Okay, so, we've lowered our expectations for this software, now what?
---------------------------------------------------------------------

Well, I guess a review of the section shema and implemented methods is in order. 

A section object conists of a django model with three attributes, all of the methods inherited from django.models.Model plus an additional create method, and finally a meta class for describing the model's metadata.

.. currentmodule:: rsum.home.models.section

.. autoclass:: Section
