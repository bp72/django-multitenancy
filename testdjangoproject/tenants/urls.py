from django.urls import path

from tenants.views import tenant_view


urlpatterns = [
    path("tenant/", tenant_view, name="tenant_views"),
]
