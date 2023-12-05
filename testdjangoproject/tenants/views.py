from django.http import HttpResponse, JsonResponse
from django_multitenancy.helpers import get_tenant_model, TENANT_VAR


def get_tanent_model_view(request):
    model = get_tenant_model()
    html = f"<html><body><h1>{model.__name__}</h1><h2>{request}</h2></body></html>"
    return HttpResponse(html, content_type="text/html", status=200)


def get_tenant_var_view(request):
    html = f"tenant: {TENANT_VAR.get()}"
    return HttpResponse(html, content_type="text/html", status=200)


def tenant_api__get_tenant_id(request):
    tenant = TENANT_VAR.get()
    return JsonResponse({
        "tenant_id": tenant.id,
    })
