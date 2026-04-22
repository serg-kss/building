from django.db import models


class PageSEO(models.Model):

    PAGE_CHOICES = (
        ("home", "Головна сторінка"),
        ("about", "Про компанію"),
        ("contact", "Контакти"),
        ("services", "Сторінка Послуг"),
        ("portfolio", "Портфоліо"),
        ("gallery", "Галерея"),
    )

    OG_TYPE_CHOICES = (
        ("website", "Website"),
        ("article", "Article"),
    )

    ROBOTS_CHOICES = (
        ("index, follow", "Index, Follow"),
        ("noindex, follow", "NoIndex, Follow"),
        ("index, nofollow", "Index, NoFollow"),
        ("noindex, nofollow", "NoIndex, NoFollow"),
    )

    TWITTER_CARD_CHOICES = (
        ("summary", "Summary"),
        ("summary_large_image", "Summary Large Image"),
    )

    SCHEMA_TYPE_CHOICES = (
        ("Organization", "Organization"),
        ("Service", "Service"),
        ("CreativeWork", "CreativeWork"),
        ("WebPage", "WebPage"),
    )

    page = models.CharField(
        "Сторінка",
        max_length=50,
        choices=PAGE_CHOICES,
        blank=True,
        null=True,
        unique=True
    )

    slug = models.SlugField(
        "Slug сторінки",
        max_length=255,
        blank=True,
        null=True,
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
        "Canonical URL",
        blank=True
    )

    robots = models.CharField(
        "Robots",
        max_length=50,
        choices=ROBOTS_CHOICES,
        default="index, follow"
    )

    og_title = models.CharField(
        "OG Title",
        max_length=255,
        blank=True
    )

    og_description = models.TextField(
        "OG Description",
        blank=True
    )

    og_type = models.CharField(
        "OG Type",
        max_length=50,
        choices=OG_TYPE_CHOICES,
        default="website"
    )

    og_image = models.ImageField(
        "OG Image",
        upload_to="seo/",
        blank=True,
        null=True
    )

    og_image_width = models.PositiveIntegerField(
        "OG Image Width",
        default=1200
    )

    og_image_height = models.PositiveIntegerField(
        "OG Image Height",
        default=630
    )

    twitter_card = models.CharField(
        "Twitter Card",
        max_length=50,
        choices=TWITTER_CARD_CHOICES,
        default="summary_large_image"
    )

    schema_type = models.CharField(
        "Schema Type",
        max_length=50,
        choices=SCHEMA_TYPE_CHOICES,
        default="WebPage"
    )

    priority = models.FloatField(
        "Sitemap Priority",
        default=0.7
    )

    class Meta:
        verbose_name = "SEO сторінку"
        verbose_name_plural = "SEO сторінки"

    def __str__(self):
        return self.title or self.page or "SEO Page"