Continuous Delivery
-------------------

Currently this is a twinkle in the eye of the author, but it will be achieved.


Code Quality
------------

Before any code is accepted into the trunk for delivery to a production environment it must pass the quality tests.  We use `Codacy`_, which is the most thorough and configurable quality tool we've found. 

.. _`Codacy`: https://www.codacy.com/

.. image:: https://api.codacy.com/project/badge/Grade/e8ccc643c99147dca4fd98a8b2851451    
   :target: https://www.codacy.com/app/gahancorpcfo/rsum.application?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=gahan-corporation/rsum.application&amp;utm_campaign=Badge_Grade


`Codacy`_ also manages test coverage for us.

.. image:: https://api.codacy.com/project/badge/Coverage/e8ccc643c99147dca4fd98a8b2851451    
   :target: https://www.codacy.com/app/gahancorpcfo/rsum.application?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=gahan-corporation/rsum.application&amp;utm_campaign=Badge_Coverage


Challenges
----------

As of now the main block to continuous delivery is the inability to deploy updates to static(y) content in an automated fashion.  This is something that bears some investigation and will be dealt with prior to the next release.
