from unittest.mock import MagicMock
import pytest
from django.db import models
from django_multitenancy.helpers import get_tenant


def test_get_tenant__doesnt_exist__expect_error(mocker):
    tenant_model_mock = MagicMock()
    tenant_model_mock.objects.get.side_effect = [Exception('test.com')]
    mocker.patch("django_multitenancy.helpers.get_tenant_model", return_value=tenant_model_mock)

    with pytest.raises(Exception) as e:
        get_tenant(domain_name='test.com')


def test_get_tenant(mocker):
    tenant_mock = MagicMock()
    tenant_model_mock = MagicMock()
    tenant_model_mock.objects.get.return_value = tenant_mock
    mocker.patch("django_multitenancy.helpers.get_tenant_model", return_value=tenant_model_mock)

    assert get_tenant(domain_name='test') is tenant_mock
