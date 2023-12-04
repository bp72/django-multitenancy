from django.http import Http404
from django.utils.deprecation import MiddlewareMixin
from django_multitenancy.helpers import get_tenant, TENANT_VAR
from django_multitenancy.mixins import TenantMixin


class MultiTenantMiddleware(MiddlewareMixin):
    TENANT_DOESNOT_EXIST_EXCEPTION = Http404

    def __init__(self, get_response):
        super().__init__(get_response)
        self.token = None

    def process_request(self, request):
        host = request.get_host()
        try:
            tenant = get_tenant(host)
            self.token = TENANT_VAR.set(tenant)
        except TenantMixin.TenantDoesNotExist:
            raise self.TENANT_DOESNOT_EXIST_EXCEPTION(f"Tenant does not exist for host '{host}'")

    def process_response(self, request, response):
        if self.token is not None:
            TENANT_VAR.reset(self.token)
        return response
