from django.conf import settings
from django.core.exceptions import ImproperlyConfigured


try:
    from django.apps import apps
    get_model = apps.get_model
except ImportError:
    from django.db.models.loading import get_model


def get_tenant_model():
    return get_model(settings.TENANT_MODEL)


def get_tenant(domain_name):
    """
    1. Реализован метод для получения тенанта по домену
    2. Добавлены юнит-тесты для метода в директории tests в корне
    3. Добавлена настройка TENANT_MODEL в testdjangoproject
    4. Добавлен тест в testdjangoproject/tests/ на то, что метод
       для получения модели из пункта 2 возвращает модель tenants.Tenant.
    """
    try:
        model = get_tenant_model()
        tenant = model.objects.get(domain_name=domain_name)
        return tenant
    except ImproperlyConfigured as E:
        raise Exception(E)
    except model.DoesNotExist:
        raise model.TenantDoesNotExist(domain_name)
