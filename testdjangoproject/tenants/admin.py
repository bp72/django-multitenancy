from django.contrib import admin
from tenants.models import Tenant


class TenantAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'domain_name', 'database_name')
    list_display_links = ('pk', 'name')


admin.site.register(Tenant, TenantAdmin)
