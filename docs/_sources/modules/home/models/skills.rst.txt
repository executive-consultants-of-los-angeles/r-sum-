Home Skills Model
==================

Skills are a bit of a special case on account of the way in which they're handled by the interpreter.

Okay, what's so special then?
-----------------------------

At the center of the representation of skills is the simple idea that one can roughly guage their relative level of proficiency in a particular area by defining how long they have been working in that area.  Obviously, this is far from a complete representation of the skills or people in question, but it does allow for the communication of what would otherwise be very difficult to describe accurately.

The credit for the progress bar animation goes to whoever it is that wrote the css for the site, which was certainly not the author of this document.  That author is pretty confident in the parity of those little graphics with what's actually the case and the reason for that is the formula for their calculation.

Formula for their calulcation? Isn't this a résumé application?
...............................................................

This is indeed a résumé application, and yes, I did say formula for their calculation.  The formula is this as follows:

let total years experience = t

let number of years for a particular skill = s

let level of skill in an area = l

If you set up an equation in which t is the dividend and s is the divisor, then oppose them to l you will create something like this:

s / t = l

Because the values s and t are (in theory, at least) known to the creator of the résumé in question the only unknown value is l.  And that means that you can solve for l in the above equation to get a floating point value which is easily convertible into a percentage.  That percentage can then be stored with the rest of the skill's data and sent on to the template for final display in the progress bar. 


Fancy!
------

Not really, but flattery is always welcome.  The algorithm for this calculation is not particularly well implemented.  It certainly won't be winning any awards for elegance in the future. 


Okay, so it's ugly, that doesn't mean it can't be tested.
---------------------------------------------------------

No, it certainly does not.

But what is there to test?
--------------------------

The Skills class is not a database model, though it is stored in the models package.  As of this writing the class contains three methods, the init, a method to calculate skills and another to calculate sub skills.  These three methods are implemented poorly, and really should be split into something more like six methods.  Currently the only possible unit tests are for the results of these three methods.  The init should generate an a new instance of the Skills object, the calculate skills method is meant to return a representation of the skills in the résumé as well as the sub-skills calculated by the method for calculating those.

This means the tests for the code as written are one to test the instantiation, one to test the calculate skills method, and one to test the calculate sub skills method.

What should it look like instead?
.................................

The calculation for the percentage should be a parameterized method in the class separate from the two other methods.  This new method could be tested against its ability to calculate the percentage correctly within acceptable precision.

.. automodule:: home.models.skills
