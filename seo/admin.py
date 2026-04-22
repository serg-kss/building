from django.contrib import admin
from django.utils.html import format_html

from seo.models import PageSEO


@admin.register(PageSEO)
class PageSEOAdmin(admin.ModelAdmin):

    list_display = (
        "page",
        "slug",
        "title",
        "robots",
        "priority",
        "image_preview",
    )

    readonly_fields = (
        "image_preview",
    )

    fieldsets = (

        ("📄 Основне SEO", {
            "fields": (
                "page",
                "title",
                "description",
                "canonical",
                "robots",
            )
        }),

        ("🌐 OpenGraph (соцмережі)", {
            "fields": (
                "og_title",
                "og_description",
                "og_type",
                "og_image",
                "image_preview",
                (
                    "og_image_width",
                    "og_image_height",
                ),
            )
        }),

        ("🐦 Twitter", {
            "fields": (
                "twitter_card",
            )
        }),

        ("📊 Schema та Sitemap", {
            "fields": (
                "schema_type",
                "priority",
            )
        }),
    )

    search_fields = (
        "title",
        "page",
    )

    list_filter = (
        "robots",
        "og_type",
        "schema_type",
    )

    def image_preview(self, obj):

        if obj.og_image:
            return format_html(
                '<img src="{}" '
                'style="max-height:120px;border-radius:6px;" />',
                obj.og_image.url
            )

        return "—"

    image_preview.short_description = "Preview"