from django.contrib import admin
from django.utils.html import format_html
from seo.models import PageSEO

# Register your models here.
@admin.register(PageSEO)
class PageSEOAdmin(admin.ModelAdmin):

    list_display = (
        "page",
        "title",
        "image_preview"
    )

    readonly_fields = (
        "image_preview",
    )

    fields = (
        "page",
        "title",
        "description",
        "canonical",
        "og_title",
        "og_description",
        "og_image",
        "image_preview",
    )

    def image_preview(self, obj):
        if obj.og_image:
            return format_html(
                '<img src="{}" style="max-height:120px;border-radius:6px;" />',
                obj.og_image.url
            )
        return "—"

    image_preview.short_description = "Preview"