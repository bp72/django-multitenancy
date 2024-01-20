================
django-multitenancy
================

.. image:: https://img.shields.io/pypi/v/django-multitenancy.svg
    :target: https://pypi.org/project/django-multitenancy
    :alt: PyPI version

.. image:: https://img.shields.io/pypi/pyversions/django-multitenancy.svg
    :target: https://pypi.org/project/django-multitenancy
    :alt: Python versions

A library that implements usage of multiple databases for multitenant django applications.

----

Concept
-------
Software multitenancy is a software architecture in which a single 
instance of software runs on a server and serves multiple tenants. 
Systems designed in such manner are "shared" (rather than "dedicated" or "isolated"). 
A tenant is a group of users who share a common access with specific privileges to the 
software instance. With a multitenant architecture, a software application is designed to 
provide every tenant a dedicated share of the instance - including its data, configuration, 
user management, tenant individual functionality and non-functional properties. 

Multitenancy contrasts with multi-instance architectures, where separate software instances 
operate on behalf of different tenants.[1]
1111

Features
--------

* List of features


Requirements
------------

* django>=4,<4.3


Installation
------------

Install `django-multitenancy` via `pip`_ from `PyPI`_::

    $ pip install django-multitenancy

Usage
-----

*

Contributing
------------
Contributions are very welcome. Tests can be run with `tox`_, please ensure
the coverage at least stays the same before you submit a pull request.

License
-------

Distributed under the terms of the `MIT`_ license, "django-multitenancy" is free and open source software


Issues
------

If you encounter any problems, please `file an issue`_ along with a detailed description.

.. _`MIT`: http://opensource.org/licenses/MIT
.. _`file an issue`: https://github.com/bp72/django-multitenancy/issues
.. _`tox`: https://tox.readthedocs.io/en/latest/
.. _`pip`: https://pypi.org/project/pip/
.. _`PyPI`: https://pypi.org/project
