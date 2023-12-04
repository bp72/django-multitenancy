"""
URL configuration for testdjangoproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from tenants.views import get_tanent_model_view, get_tenant_var_view, tenant_api__get_tenant_id

urlpatterns = [
    path("admin/", admin.site.urls),
    path("tenant_model", get_tanent_model_view),
    path("tenant_var", get_tenant_var_view),
    path("tenant/get/id", tenant_api__get_tenant_id),
]
