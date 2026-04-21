from django.contrib import admin
from adminsortable2.admin import SortableAdminBase, SortableInlineAdminMixin
from main.admin_mixins import SingletonAdmin
from services.models import Service, ServiceCapabilities, ServiceDetailsData, ServiceMethodology, ServicePage, ServicePageExtraServices


class ServicePageExtraServicesInline(SortableInlineAdminMixin, admin.StackedInline):
    model = ServicePageExtraServices
    extra = 0
    ordering = ("order",)

    fieldsets = (
        ("- Доп послуги", {
            "fields": (
                "option_title",
                "option_text",
            )
        }),

    )


@admin.register(ServicePage)
class ServicePagedmin(SortableAdminBase, SingletonAdmin):
    class Media:
        css = {
            "all": ("assets/css/admin.css",)
        }

    inlines = [ServicePageExtraServicesInline]

    fieldsets = (
        ("Інформація на сторінці", {
            "fields": (
                "h1", 
                "sub_title",
                "sub_text",
                "img_main",
                "img_main_alt",)
        }),
    )






class ServiceDetailsDataInline(SortableInlineAdminMixin, admin.StackedInline):
    model = ServiceDetailsData
    extra = 0
    ordering = ("order",)

    fieldsets = (
        ("- Доп інформація", {
            "fields": (
                "key",
                "feture",
            )
        }),

    )


class ServiceMethodologyInline(SortableInlineAdminMixin, admin.StackedInline):
    model = ServiceMethodology
    extra = 0
    ordering = ("order",)

    fieldsets = (
        ("- Методологіі", {
            "fields": (
                "title",
                "text",
                "option_1",
                "option_2",
                "option_3",
            )
        }),

    )


class ServiceCapabilitiesInline(SortableInlineAdminMixin, admin.StackedInline):
    model = ServiceCapabilities
    extra = 0
    ordering = ("order",)

    fieldsets = (
        ("- Можливості", {
            "fields": (
                "title",
                "text",
            )
        }),

    )


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin, SortableAdminBase,):
    class Media:
        css = {
            "all": ("assets/css/admin.css",)
        }
    
    inlines = [ServiceDetailsDataInline, ServiceMethodologyInline, ServiceCapabilitiesInline]

    fieldsets = (
        ("Картка послуги", {
            "fields": (
                "name",
                "slug",
                "sub_text",
                "option_1",
                "option_2",
                "option_3",
                )
        }),

        ("Детальна інформація", {
            "fields": (
                "content",
                "img_main",
                "img_main_alt",
                "title",
                "text",
            )
        }),
    )
