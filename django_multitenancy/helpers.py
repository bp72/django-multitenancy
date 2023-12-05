from contextvars import ContextVar
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured


try:
    from django.apps import apps
    get_model = apps.get_model
except ImportError:
    from django.db.models.loading import get_model


TENANT_VAR = ContextVar("django_multitenancy_tenant")


def get_tenant_model():
    return get_model(settings.TENANT_MODEL)


def get_tenant(domain_name):
    """
    Get Tenant Instance by domain name. It raises 2 kind of exceptions:
    1. ImproperlyConfigured in case of any problem with get_model
    2. TenantDoesNotExist if there is no tenant by domain
    """
    try:
        model = get_tenant_model()
        tenant = model.objects.get(domain_name=domain_name)
        return tenant
    except ImproperlyConfigured as E:
        raise Exception(E)
    except model.DoesNotExist:
        raise model.TenantDoesNotExist(domain_name)
