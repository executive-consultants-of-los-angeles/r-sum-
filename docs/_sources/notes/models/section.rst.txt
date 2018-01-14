home.models.section
...................

Here will be a brief but complet e discussion of the properties and attributes of the section model.

Just what is a section anyway?
------------------------------

In this context a section is the first level of categorization applied to a person's c.v.  That is to say, there is the c.v. as a holistic entity, then that is (generally) broken up into constituent parts in order to tell a story that presents the most appealing version of the subject as possible. 

There are further divisions of the data in a c.v., but implementing them in a relational database is clumsy and awkward.  Or at least the author isn't smart enough to make it not clumsy and awkward.  For the sake of this software, there will be only the two layers: the document itself and its sections. 

Okay, so, we've lowered our expectations for this software, now what?
---------------------------------------------------------------------

Well, I guess a review of the section shema and implemented methods is in order. 

A section object conists of a django model with three attributes, all of the methods inherited from django.models.Model plus an additional create method, and finally a meta class that sets the app label and any other options that may be required.

Section Fields
..............

:profile: A link to the relevant Profile.
:name: The name of the section.
:content: The content of the section stored in JSON.

.. currentmodule:: home.models.section

.. autoclass:: Section
   :members:

Finally, how do we write unit tests for a Section object?
---------------------------------------------------------

This should be relatively simple I think.  We can start with instantiating a section object and checking that it's got all of the required attributes.  Then we can test each attribute to be sure that it is of the correct type. Finally, we can run the create method for a section then check that it is stored in the database.
