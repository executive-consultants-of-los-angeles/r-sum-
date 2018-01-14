home.models.profile
===================

What do we mean by profile?
---------------------------

A profile is a curriculum vitae for an individual that presents their pervious work such that it demonstrates their experience and skill.

Why don't we just call it a résumé like everyone else?
------------------------------------------------------

Because everyone else *actually* calls it a resume, which is nothing at all like a résumé.  Also, there is no key for the `é` character available on the author's keyboard. This means that in order to type `é` the author has to go out of his way to print the 'special' character by entering a special mode in his text editor.  Persumably this is also why most people call it a resume instead of a résumé.  Finally, because the programming languages this is written in, much like the author's text editor, don't really handle 'special' characters like the `é` very well and most folks these days don't spend too much time learning Latin, that the best way to describe what the program is trying to make ready is the word profile.

Right, so, that's pretty dumb. What's the object look like?
-----------------------------------------------------------

Also pretty dumb.  The only attributes the Profile object contains are the name and the content.

Profile Fields
..............

:name: The name of the current Profile object.
:content: The unmodified JSON encoded content read from a yaml file.

Okay, so it ought to be pretty easy to test then, yeah?
-------------------------------------------------------

The author believes so, yes.  It should require just the three tests: one for instantion of Profile objects, one for the attributes of the object, and one to test the create method.

The third test should be the hardest to write since it involves checking the related section objects.
