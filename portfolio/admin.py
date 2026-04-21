from django.contrib import admin
from adminsortable2.admin import SortableAdminBase, SortableInlineAdminMixin
from django.utils.html import format_html

from main.admin_mixins import SingletonAdmin
from portfolio.models import Portfolio, PortfolioDetailsData, PortfolioPage, TechnicalDetails, PortfolioImage


class PortfolioDetailsDataInline(SortableInlineAdminMixin, admin.StackedInline):
    model = PortfolioDetailsData
    extra = 0
    ordering = ("order",)

    fieldsets = (
        ("- Інформація про обʼєкт", {
            "fields": (
                "key",
                "feture",
            )
        }),

    )


class TechnicalDetailsInline(SortableInlineAdminMixin, admin.StackedInline):
    model = TechnicalDetails
    extra = 0
    ordering = ("order",)

    readonly_fields = (
        "preview",
    )

    fieldsets = (
        ("- Інформація про обʼєкт", {
            "fields": (
                "doc_name",
                "slug",
                "doc_content",
                "img_doc",
                "img_doc_alt",
            )
        }),

    )
    def preview(self, obj):
        if obj.img_doc:
            return format_html(
                '<img src="{}" style="height:90px;border-radius:6px;" />',
                obj.img_doc.url
            )
        return "—"

class PortfolioImageInline(SortableInlineAdminMixin, admin.StackedInline):
    model = PortfolioImage
    extra = 0
    ordering = ("order",)

    readonly_fields = (
        "preview",
    )

    fieldsets = (
        ("- Інформація про обʼєкт", {
            "fields": (
                "image",
                "alt_text",
            )
        }),

    )
    def preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="height:90px;border-radius:6px;" />',
                obj.image.url
            )
        return "—"
    

@admin.register(Portfolio)
class PortfolioAdmin(SortableAdminBase, admin.ModelAdmin):

    class Media:
        css = {
            "all": ("assets/css/admin.css",)
        }

    inlines = [PortfolioDetailsDataInline, TechnicalDetailsInline, PortfolioImageInline]

    fieldsets = (
        ("Картка проекта", {
            "fields": (
                "status", 
                "name",
                "slug",
                "type",
                "content_brif",
                "img",
                "img_alt",
                "option_1",
                "option_2",
                "location")
        }),

        ("Детальна інформація", {
            "fields": (
                "option_3",
                "option_4",
                "content",
                "img_main",
                "img_main_alt",
            )
        }),
    )

    readonly_fields = ("image_preview",)

    def image_preview(self, obj):
        images_html = []

        # основные изображения
        if obj.img:
            images_html.append(
                format_html(
                    '<img src="{}" style="height:120px;border-radius:6px;margin:5px;">',
                    obj.img.url
                )
            )

        if obj.img_main:
            images_html.append(
                format_html(
                    '<img src="{}" style="height:120px;border-radius:6px;margin:5px;">',
                    obj.img_main.url
                )
            )

        if not images_html:
            return "—"

        return format_html(
            '<div style="display:flex;flex-wrap:wrap;">{}</div>',
            format_html("".join(images_html))
        )

    image_preview.short_description = "Попередній перегляд"


@admin.register(PortfolioPage)
class PortfolioPageAdmin(SortableAdminBase, SingletonAdmin):
    class Media:
        css = {
            "all": ("assets/css/admin.css",)
        }