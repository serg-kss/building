from main.admin_mixins import SingletonAdmin
from .models import AboutPage, ContactsData, Gallery, HomePage, HomePageCertifCreator, Privacy, SocialMedia, ContactMessages, TeamAboutPage, Terms, TestimonialsAboutPage, AboutImage
from django.utils.html import format_html
from adminsortable2.admin import SortableInlineAdminMixin, SortableAdminBase
from django.contrib import admin


@admin.register(ContactsData)
class ContactsDataAdmin(SingletonAdmin):
    class Media:
        css = {
            "all": ("assets/css/admin.css",)
        }


@admin.register(SocialMedia)
class SocialMediaAdmin(SingletonAdmin):
    class Media:
        css = {
            "all": ("assets/css/admin.css",)
        }


@admin.register(ContactMessages)
class ContactMessagesAdmin(admin.ModelAdmin):
    class Media:
        css = {
            "all": ("assets/css/admin.css",)
        }

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


class HomePageCertifCreatorInline(SortableInlineAdminMixin, admin.StackedInline):
    model = HomePageCertifCreator
    extra = 0
    readonly_fields = (
        "preview",
    )

    class Media:
        css = {
            "all": ("assets/css/admin.css",)
        }
    fieldsets = (
        ("- Зображення сертифікатів або нагород ", {
            "fields": (
                "title",
                "sub_title",
                "text",
                "img",
                "preview",
                "alt_img",
            )
        }),
    )

    def preview(self, obj):
        if obj.img:
            return format_html(
                '<img src="{}" style="height:90px;border-radius:6px;" />',
                obj.img.url
            )
        return "—"


@admin.register(HomePage)
class HomePageAdmin(SortableAdminBase, SingletonAdmin):

    class Media:
        js = ("assets/js/admin.js",)
        css = {
            "all": ("assets/css/admin.css",)
        }
    inlines = [HomePageCertifCreatorInline]
    fieldsets = (
        ("Блок: Вступ", {
            "fields": (
                "h1", 
                "hero_text",
                "hero_years_experience",
                "hero_projects_completed",
                "hero_satisfied_clients",
                "hero_img",
                "hero_img_alt",
                "hero_video"
                )
        }),
        ("Блок: Послуги", {
            "fields": (
                "sub_title_services",
                "sub_text_services",
            )
        }),
        ("Блок: Проекти", {
            "fields": (
                "sub_title_portfolio",
                "sub_text_portfolio",
            )
        }),
        ("Блок: Сертифікати", {
            "fields": (
                "sub_title_certif",
                "sub_text_certif",
                "title_certif",
                "text_certif",
                "img_certif",
                "img_certif_alt",
                "title_certif_img",
                'text_certif_img',
                "awards_certif",
            )
        }),
        ("Блок: Команда", {
            "fields": (
                "sub_title_team",
                "sub_text_team",
            )
        }),
        ("Блок: Підтримка клієнтів", {
            "fields": (
                "title_quote",
                "text_quote",
                "option_1",
                "option_2",
                "option_3",
            )
        }),
    )


class AboutImageInline(SortableInlineAdminMixin, admin.StackedInline):
    model = AboutImage
    extra = 0
    readonly_fields = (
        "preview",
    )

    class Media:
        css = {
            "all": ("assets/css/admin.css",)
        }
    fieldsets = (
        ("- Зображення сертифікатів або нагород ", {
            "fields": (
                "image",
                "preview",
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


class TeamAboutInline(SortableInlineAdminMixin, admin.StackedInline):
    model = TeamAboutPage
    extra = 0
    ordering = ("order",)
    verbose_name = "Учасник команди"
    verbose_name_plural = "Учасники команди"

    readonly_fields = (
        "preview",
    )

    fieldsets = (
        ("- Інформація про учасника команди", {
            "fields": (
                "team_name",
                "team_position",
                "team_description",
            )
        }),

        ("- Соц мережі", {
            "fields": (
                "email",
                "phone",
                "linkedin",
                "option_1",
                "option_2",
            )
        }),

        ("- Інше", {
            "fields": (
                "team_img",
                "preview",
            )
        }),
    )

    def preview(self, obj):
        if obj.team_img:
            return format_html(
                '<img src="{}" style="height:90px;border-radius:6px;" />',
                obj.team_img.url
            )
        return "—"
    

class TestimonialAboutInline(SortableInlineAdminMixin, admin.StackedInline):
    model = TestimonialsAboutPage
    extra = 0
    ordering = ("order",)

    readonly_fields = (
        "preview",
    )

    fieldsets = (
        ("- Інформація про відгук", {
            "fields": (
                "testimonials_name",
                "testimonials_position",
                "testimonials_company",
                "testimonials_message",
            )
        }),

        ("- Інше", {
            "fields": (
                "testimonials_img",
                "preview",
                "order",
            )
        }),
    )

    def preview(self, obj):
        if obj.testimonials_img:
            return format_html(
                '<img src="{}" style="height:90px;border-radius:6px;" />',
                obj.testimonials_img.url
            )
        return "—"


@admin.register(AboutPage)
class AboutPageAdmin(SortableAdminBase, SingletonAdmin):

    class Media:
        css = {
            "all": ("assets/css/admin.css",)
        }

    inlines = [AboutImageInline, TeamAboutInline, TestimonialAboutInline]

    fieldsets = (
        ("Сторінка про компанію", {
            "fields": ("h1_about", "h1_team")
        }),

        ("Блок історії", {
            "fields": (
                "h2",
                "history_text",
                "history_img_left",
                "alt_img_left",
                "history_img_right",
                "alt_img_right",
                "image_preview",
                "history_video",
            )
        }),
        ("Блок статистики", {
            "fields": (
                (
                    "years_number_statistics",
                    "projects_number_statistics",
                ),
                (

                    "workers_number_statistics",
                ),
            )
        }),
    )

    readonly_fields = ("image_preview",)

    def image_preview(self, obj):
        images_html = []

        # основные изображения
        if obj.history_img_left:
            images_html.append(
                format_html(
                    '<img src="{}" style="height:120px;border-radius:6px;margin:5px;">',
                    obj.history_img_left.url
                )
            )

        if obj.history_img_right:
            images_html.append(
                format_html(
                    '<img src="{}" style="height:120px;border-radius:6px;margin:5px;">',
                    obj.history_img_right.url
                )
            )

        if not images_html:
            return "—"

        return format_html(
            '<div style="display:flex;flex-wrap:wrap;">{}</div>',
            format_html("".join(images_html))
        )

    image_preview.short_description = "Попередній перегляд"


@admin.register(Terms)
class TermsAdmin(SingletonAdmin):
    class Media:
        css = {
            "all": ("assets/css/admin.css",)
        }


@admin.register(Privacy)
class PrivacyAdmin(SingletonAdmin):
    class Media:
        css = {
            "all": ("assets/css/admin.css",)
        }


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    class Media:
        css = {
            "all": ("assets/css/admin.css",)
        }
    readonly_fields = ("preview",)

    list_display = (
        "preview",
    )
    
    fieldsets = (
        ("Сторінка про компанію", {
            "fields": (
                "title",
                "text",
                "img", 
                "alt_img",
            )
        }),
    )
    def preview(self, obj):
        if obj.img:
            return format_html(
                '<img src="{}" style="height:90px;border-radius:6px;" />',
                obj.img.url
            )
        return "—"
    
    preview.short_description = "Попередній перегляд"
