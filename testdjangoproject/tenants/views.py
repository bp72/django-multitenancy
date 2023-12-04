from django.http import HttpResponse
from django_multitenancy.helpers import get_tenant_model


def get_tanent_model_view(request):
    model = get_tenant_model()
    html = f"<html><body><h1>{model.__name__}</h1><h2>{request}</h2></body></html>"
    return HttpResponse(html, content_type="text/html", status=200)
