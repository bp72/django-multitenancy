from django.db import models

from django_multitenancy.mixins import TenantMixin


class Tenant(TenantMixin):
    name = models.CharField(max_length=100, null=False)
