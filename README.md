# Django Multitenancy

![Django Multitenancy](path/to/your/diagram.png)

django-multitenancy is a Django library that enables multitenancy in your web applications. 

Multitenancy is a software architecture where a single instance of an application serves multiple tenants, or clients, in a shared environment. In this model, tenants share the same application and underlying infrastructure, but their data is logically/phisically isolated, allowing each tenant to operate as if they have their own dedicated instance. Typically, multitenancy is employed to optimize resource utilization and reduce operational costs by serving a large user base with a single, shared codebase and set of resources.

In the solution with a shared common database and separate database per tenant, a central database stores common data shared among all tenants, promoting resource efficiency, while each tenant has its own dedicated database for customized and isolated data management. This architecture provides a balance between shared resource benefits and individual tenant autonomy, making it well-suited for applications where tenants require varying levels of customization and data isolation. However, it introduces increased complexity in database management as each tenant's database needs separate administration


## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
  - [Configuring Multitenancy](#configuring-multitenancy)
  - [Defining Tenant-Specific Models](#defining-tenant-specific-models)
  - [Accessing Tenant-Specific Data](#accessing-tenant-specific-data)
  - [Example](#example)
- [Contributing](#contributing)
- [License](#license)

## Installation

To install the `django-multitenancy` package, use the following pip command:

```bash
pip install django-multitenancy
```

## Usage

### Configuring Multitenancy

In your Django project's settings, add `multitenancy` to your `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    # ...
    'multitenancy',
    # ...
]
```

Include the `TenantMiddleware` in your `MIDDLEWARE`:

```python
MIDDLEWARE = [
    # ...
    'multitenancy.middleware.TenantMiddleware',
    # ...
]
```

### Defining Tenant-Specific Models

Create tenant-specific models by inheriting from `multitenancy.models.TenantModel`:

```python
from multitenancy.models import TenantModel

class TenantSpecificModel(TenantModel):
    # Your model fields here
    name = models.CharField(max_length=255)
```

### Accessing Tenant-Specific Data

To access tenant-specific data, use the `TenantManager`:

```python
from multitenancy.managers import TenantManager

class YourModel(models.Model):
    # Your model fields here
    name = models.CharField(max_length=255)
    
    # Use the TenantManager for tenant-specific queries
    objects = TenantManager()
```

### Example

Here's a simple example of using Django Multitenancy in a view:

```python
from django.shortcuts import render
from .models import TenantSpecificModel

def your_view(request):
    # Get tenant-specific data using the TenantManager
    data = TenantSpecificModel.objects.all()

    return render(request, 'your_template.html', {'data': data})
```

For a more detailed example, check the [examples](examples/) directory in this repository.

## Contributing

We welcome contributions! Please follow our [contribution guidelines](CONTRIBUTING.md) to get started.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.




A library that implements usage of multiple databases for multitenant django applications.

----

Concept
-------
Software multitenancy is a software architecture in which a single instance of software runs on a server and serves multiple tenants. 

Systems designed in such manner are "shared" (rather than "dedicated" or "isolated"). 

A **tenant** is a group of users who share a common access with specific privileges to the 
software instance. 

With a multitenant architecture, a software application is designed to 
provide every tenant a dedicated share of the instance - including its data, configuration, 
user management, tenant individual functionality and non-functional properties. 

Multitenancy contrasts with multi-instance architectures, where separate software instances 
operate on behalf of different tenants.


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
