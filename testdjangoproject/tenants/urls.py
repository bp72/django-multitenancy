from django.urls import path

from tenants.views import (
    get_tanent_model_view,
    get_tenant_var_view,
    tenant_api__get_tenant_id,
)


urlpatterns = [
    path("tenant/model", get_tanent_model_view, name="tenant-model-view"),
    path("tenant/var", get_tenant_var_view, name="tenant-var-view"),
    path("tenant/get-id", tenant_api__get_tenant_id, name="tenant-get-id"),
]
