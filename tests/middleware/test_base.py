from unittest.mock import MagicMock
import pytest
from django.db import models
from django_multitenancy.helpers import get_tenant
from django_multitenancy.middleware import MultiTenantMiddleware


@pytest.mark.django_db
def test_middleware__tenant_does_not_exist(rf):
    get_response = MagicMock()
    request = rf.get(
        '/',
        headers={"host": "example.com"},
    )

    with pytest.raises(Exception) as e:    
        middleware = MultiTenantMiddleware(get_response)
        response = middleware(request)
        assert response.status_code == 404
    

@pytest.mark.django_db
def test_middleware__tenant_ok__WIP(rf):
    get_response = MagicMock()
    request = rf.get(
        '/',
        headers={"host": "example.com"},
    )

    with pytest.raises(Exception) as e:    
        middleware = MultiTenantMiddleware(get_response)
        response = middleware(request)
        assert response.status_code == 404

