from tenants.models import Tenant


class TestTenant:

    def test_init(self, db):
        tenant = Tenant.objects.create(
            name="New tenant",
            database_name="tenant",
            domain_name="tenant.com",
        )

        created_tenant = Tenant.objects.get(id=tenant.id)
        assert created_tenant.name == "New tenant"
        assert created_tenant.database_name == "tenant"
        assert created_tenant.domain_name == "tenant.com"
