from django.test.client import RequestFactory
import pytest
from django.db import models
from django_multitenancy.helpers import get_tenant
from django_multitenancy.middleware import MultiTenantMiddleware
from unittest.mock import MagicMock


def test_middleware__host_no_www_prefix(rf: RequestFactory):
    get_response = MagicMock()
    request = rf.get('/', headers={"host": "example.com"})
    middleware = MultiTenantMiddleware(get_response)
    host = middleware.get_hostname(request=request)
    assert host == "example.com"

def test_middleware__host_with_www_prefix(rf: RequestFactory):
    get_response = MagicMock()
    request = rf.get('/', headers={"host": "www.example.com"})
    middleware = MultiTenantMiddleware(get_response)
    host = middleware.get_hostname(request=request)
    assert host == "example.com"


@pytest.mark.django_db
def test_middleware__tenant_does_not_exist(rf: RequestFactory):
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
def test_middleware__tenant_ok__WIP(rf: RequestFactory, mocker):
    get_response = MagicMock()
    response = MagicMock()
    response.json.return_value = {"tenant_id": 123}
    response.status_code = 200

    get_response.return_value = response

    request = rf.get('/', headers={"host": "example.com"})
    
    tenant_mock = MagicMock()
    tenant_mock.id.return_value = 123
    tenant_mock.name.return_value = "example"
    tenant_mock.domain_name.return_value = "example.com"
    
    tenant_model_mock = MagicMock()
    tenant_model_mock.objects.get.return_value = tenant_mock
    
    mocker.patch("django_multitenancy.helpers.get_tenant_model", return_value=tenant_model_mock)

    middleware = MultiTenantMiddleware(get_response)
    resp = middleware(request)
    assert resp is response
    assert resp.json() == {"tenant_id": 123}
    assert resp.status_code == 200
