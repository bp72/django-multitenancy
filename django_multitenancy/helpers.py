import os
from contextlib import ContextDecorator
from functools import lru_cache, wraps
from types import ModuleType

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured, ValidationError
from django.db import DEFAULT_DB_ALIAS, connection, connections
from django.utils.module_loading import import_string

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
    model = get_tenant_model()
    try:
        tenant = model.objects.get(domain_name=domain_name)
        if tenant is None:
            raise Exception("test2")
        return tenant
    except ImproperlyConfigured as E:
        raise Exception(E)
    except model.DoesNotExist:
        raise Exception("bomj")
