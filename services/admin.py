from django.contrib import admin
from adminsortable2.admin import SortableAdminBase
from services.models import Service

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin, SortableAdminBase,):
    class Media:
        css = {
            "all": ("assets/css/admin.css",)
        }
