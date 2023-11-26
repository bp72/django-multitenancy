import json

from django_multitenancy.context import current_tenant
from django.http.response import HttpResponse


def tenant_view(request):
    tenant = current_tenant.get()
    return HttpResponse(json.dumps({"tenant_id": tenant.id}))
