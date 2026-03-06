from django.contrib import admin

from main.admin_mixins import SingletonAdmin
from .models import ContactsData, HomePageSeo, HomeSlider, SocialMedia, ContactMessages
from django.utils.html import format_html

from adminsortable2.admin import SortableInlineAdminMixin, SortableAdminBase

@admin.register(ContactsData)
class ContactsDataAdmin(SingletonAdmin):
    pass

@admin.register(SocialMedia)
class SocialMediaAdmin(SingletonAdmin):
    pass

@admin.register(ContactMessages)
class ContactMessagesAdmin(admin.ModelAdmin):

    list_display = ("name", "email", "subject", "created_at", "is_read")

    list_filter = ("is_read", "created_at")

    readonly_fields = (
        "name",
        "email",
        "subject",
        "message",
        "created_at",
    )
    def get_read_status(self, obj):
        if not obj.is_read:
            return "🔴 Нове"
        return "✓"

    search_fields = ("name", "email", "subject")

    def has_add_permission(self, request):
        return False


class HomeSliderInline(SortableInlineAdminMixin, admin.StackedInline):
    model = HomeSlider
    extra = 0
    ordering = ("order",)

    readonly_fields = (
        "preview_desktop",
        "preview_mobile",
    )

    fieldsets = (
        ("- Відображення для ноутбука", {
            "fields": (
                "image",
                "preview_desktop",
            )
        }),

        ("- Відображення для смартфону", {
            "fields": (
                "image_mobile",
                "preview_mobile",
            )
        }),

        ("- Інфо", {
            "fields": (
                "alt",
                "order",
            )
        }),
    )

    def preview_desktop(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="height:90px;border-radius:6px;" />',
                obj.image.url
            )
        return "—"

    preview_desktop.short_description = "Попередній перегляд"

    def preview_mobile(self, obj):
        if obj.image_mobile:
            return format_html(
                '<img src="{}" style="height:90px;border-radius:6px;" />',
                obj.image_mobile.url
            )
        return "—"

    preview_mobile.short_description = "Попередній перегляд (смарт)"



@admin.register(HomePageSeo)
class HomePageSeoAdmin(SortableAdminBase, SingletonAdmin):
    inlines = [HomeSliderInline]