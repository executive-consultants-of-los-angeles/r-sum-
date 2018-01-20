Continuous Integration
----------------------

.. note:: draft


`Travis CI`_
............

.. _Travis CI: https://travis-ci.org


We use Travis CI for integration on all of our projects.  It's the simplest and most effective tool that we've tried for integration, so it's the one we use by default.  

Gahan Corporation's Travis profile may be `found here`_.

.. _found here: https://travis-ci.org/gahan-corporation


The history for this project is available at `this location`_.

.. _this location: https://travis-ci.org/gahan-corporation/rsum.application


Build Status
____________

.. image:: https://travis-ci.org/gahan-corporation/rsum.application.svg?branch=master
   :target: https://travis-ci.org/gahan-corporation/rsum.application


Integration Testing
-------------------

The tests are run inside a Docker container that is built on Travis for the purpose.  The test suite makes use of pytest.  Coverage is calculated using coverage.py, and the application makes use of setuptools for building and installation.

Integration tests must be passed before any code is allowed to be merged into a protected branch.  This is managed in GitHub.  


Functional Testing
------------------

Currently there is no automated functional testing.


Load Testing
------------

Currently there is no load testing.


User Interface Testing
----------------------

Also no. 
