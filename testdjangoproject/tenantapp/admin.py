from django.contrib import admin
from tenantapp.models import House


@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    list_display = ("id", "addr")
