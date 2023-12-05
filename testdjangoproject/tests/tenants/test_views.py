from django.urls import reverse

from tenants.models import Tenant


def test_tenant_view__OK(client, db):
    tenant1 = Tenant.objects.create(
        name="tenant1",
        domain_name="tenant1.com",
        database_name="tenant1"
    )
    Tenant.objects.create(
        name="tenant2",
        domain_name="tenant2.com",
        database_name="tenant2"
    )

    response = client.get(
        reverse("tenant-get-id"),
        headers={
            "Host": "tenant1.com",
        },
    )

    assert response.json() == {"tenant_id": tenant1.id}


def test_tenant_view__OK_with_www_prefix(client, db):
    tenant1 = Tenant.objects.create(
        name="tenant1",
        domain_name="tenant1.com",
        database_name="tenant1"
    )
    Tenant.objects.create(
        name="tenant2",
        domain_name="tenant2.com",
        database_name="tenant2"
    )

    response = client.get(
        reverse("tenant-get-id"),
        headers={
            "Host": "www.tenant1.com",
        },
    )

    assert response.json() == {"tenant_id": tenant1.id}


def test_tenant_view__tenant_does_not_exist_404(client, db):
    Tenant.objects.create(
        name="tenant2",
        domain_name="tenant2.com",
        database_name="tenant2"
    )
    response = client.get(
        reverse("tenant-get-id"),
        headers={
            "Host": "tenant1.com",
        },
    )

    assert response.status_code == 404
