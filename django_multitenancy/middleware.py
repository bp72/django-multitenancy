from django_multitenancy.context import current_tenant
from django_multitenancy.helpers import get_tenant


class TenantMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    @staticmethod
    def get_hostname(request) -> str:
        return request.get_host().split(':')[0].lstrip("www.")

    def __call__(self, request):
        print('hostname', self.get_hostname(request))
        tenant = get_tenant(domain_name=self.get_hostname(request))
        current_tenant.set(tenant)

        response = self.get_response(request)

        current_tenant.set(None)
        return response
