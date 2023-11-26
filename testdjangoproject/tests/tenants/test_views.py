from django.urls import reverse

from tenants.models import Tenant


def test_tenant_view(client, db):
    tenant1 = Tenant.objects.create(name="tenant1", domain_name="tenant1.com", database_name="tenant1")
    Tenant.objects.create(name="tenant2", domain_name="tenant2.com", database_name="tenant2")

    response = client.get(
        reverse("tenant_view"),
        headers={
            "Host": "tenant1.com",
        },
    )

    assert response.json() == {"tenant_id": tenant1.id}
