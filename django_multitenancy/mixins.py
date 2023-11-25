from django.db import models

from django_multitenancy.constants import POSTGRESQL_MAX_NAME_LENGTH, MAX_WEB_DOMAIN_LENGTH


class TenantMixin(models.Model):

    database_name = models.CharField(max_length=POSTGRESQL_MAX_NAME_LENGTH, unique=True)
    domain_name = models.CharField(max_length=MAX_WEB_DOMAIN_LENGTH, unique=True)

    class Meta:
        abstract = True
