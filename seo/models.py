from django.db import models


class PageSEO(models.Model):

    PAGE_CHOICES = (
        ("home", "Головна сторінка"),
        ("about", "Про компанію"),
        ("contact", "Контакти"),
        ("services", "Сторінка сервісів"),
        ("portfolio", "Портфоліо"),
    )

    page = models.CharField(
        "Сторінка",
        max_length=50,
        choices=PAGE_CHOICES,
        unique=True
    )

    title = models.CharField(
        "SEO title",
        max_length=255
    )

    description = models.TextField(
        "Meta description",
        blank=True
    )

    canonical = models.URLField(
        blank=True
    )

    og_title = models.CharField(
        max_length=255,
        blank=True
    )

    og_description = models.TextField(
        blank=True
    )

    og_image = models.ImageField(
        upload_to="seo/",
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = "SEO сторінку"
        verbose_name_plural = "SEO сторінки"

    def __str__(self):
        return self.page