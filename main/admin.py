from django.contrib import admin

from main.admin_mixins import SingletonAdmin
from .models import AboutPage, ContactsData, HomePage, HomeSlider, SocialMedia, ContactMessages
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


from django.contrib import admin, messages
from django.shortcuts import redirect
from django.urls import reverse


@admin.register(HomePage)
class HomePageAdmin(SortableAdminBase, SingletonAdmin):

    inlines = [HomeSliderInline]

    class Media:
        js = ("assets/js/admin.js",)

    def changelist_view(self, request, extra_context=None):

        obj = HomePage.objects.first()

        if obj:
            return redirect(
                reverse(
                    "admin:main_homepage_change",
                    args=[obj.id]
                )
            )

        return super().changelist_view(request, extra_context)

    def response_change(self, request, obj):

        if "_save" in request.POST:

            self.message_user(
                request,
                "Головна сторінка успішно збережена ✅",
                level=messages.SUCCESS
            )

            return redirect(reverse("admin:index"))

        return super().response_change(request, obj)


@admin.register(AboutPage)
class AboutPageAdmin(SortableAdminBase, SingletonAdmin):

    class Media:
        css = {
            "all": ("assets/css/admin.css",)
        }


    fieldsets = (
        ("Сторінка про компанію", {
            "fields": ("h1",)
        }),

        ("Блок історії", {
            "fields": (
                "h2",
                "history_text",
                "history_img",
                "image_preview",
                "history_video",
            )
        }),
        ("Блок статистики", {
            "fields": (
                "title_statistics",
                "subtitle_statistics",
                (
                    "clients_number_statistics",
                    "projects_number_statistics",
                ),
                (
                    "support_h_number_statistics",
                    "workers_number_statistics",
                ),
                "statistics_img",
            )
        }),
    )

    readonly_fields = ("image_preview",)

    def image_preview(self, obj):
        if obj.history_img:
            return format_html(
                '<img src="{}" style="max-height:200px;border-radius:6px;">',
                obj.history_img.url
            )
        return "—"
    
    def image_preview(self, obj):
        if obj.statistics_img:
            return format_html(
                '<img src="{}" style="max-height:200px;border-radius:6px;">',
                obj.statistics_img.url
            )
        return "—"

    image_preview.short_description = "Попередній перегляд"