from django.db import models
from tinymce.models import HTMLField
from django.utils.text import slugify
from main.utils.image import compress_image
from seo.models import PageSEO
from django.urls import reverse
import os
from django.conf import settings


from functools import partial


def upload_to_folder(instance, filename, folder):
    path = os.path.join(
        settings.MEDIA_ROOT,
        folder
    )

    os.makedirs(path, exist_ok=True)

    return f"{folder}/{filename}"


upload_home_portfolio = partial(upload_to_folder, folder="portfolio")

class Portfolio(models.Model):

    class Status(models.TextChoices):
        NEW = "new", "Новий"
        IN_PROGRESS = "progress", "В роботі"
        DONE = "done", "Завершено"

    status = models.CharField(
        "Статус",
        max_length=30,
        choices=Status.choices,
        default=Status.NEW,
    )    
    name = models.CharField("Назва Проекту", max_length=100, blank=True, default="")
    type = models.CharField("Тип Проекту", max_length=100, blank=True, default="")
    content_brif = models.TextField("Опис проекту (коротко)", max_length=500, blank=True, default="")
    img = models.ImageField(
        "Зображення",
        upload_to=upload_home_portfolio
    )
    img_alt = models.CharField("Опис для зображення", max_length=300, blank=True)

    slug = models.SlugField(unique=True)
    seo = models.OneToOneField(
        PageSEO,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="portfolio"
    )
    option_1 = models.CharField("Доп інфо", max_length=50, blank=True, default="")
    option_2 = models.CharField("Срок виконання", max_length=50, blank=True, default="")
    location = models.CharField("Місце розташування", max_length=100, blank=True, default="")


    option_3 = models.CharField("Доп інфо 1", max_length=50, blank=True, default="")
    option_4 = models.CharField("Доп інфо 2", max_length=50, blank=True, default="")
    content = HTMLField(
        "Опис проекту"
    )
    img_main = models.ImageField(
        "Зображення головне",
        upload_to=upload_home_portfolio
    )
    img_main_alt = models.CharField("Опис для зображення", max_length=300, blank=True)


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

        if self.img:
            compress_image(self.img.path, (1920, 900))
        if self.img_main:
            compress_image(self.img_main.path, (1920, 900))

    def get_absolute_url(self):

        return reverse(
            "portfolio:portfolio-details",
            kwargs={"slug": self.slug}
        )

    class Meta:
        verbose_name = "Портфоліо"
        verbose_name_plural = "Портфоліо"

    def __str__(self):
        return f"{self.name}"
    

class PortfolioAddInfo(models.Model):
    add_data = models.ForeignKey(
    Portfolio,
    on_delete=models.CASCADE,
    related_name="add_data"
    )

    extr_key = models.CharField("Параметр", max_length=100, blank=True, default="")
    extr_feture = models.CharField("Значення", max_length=100, blank=True, default="")
    extr_key_1 = models.CharField("Параметр", max_length=100, blank=True, default="")
    extr_feture_1 = models.CharField("Значення", max_length=100, blank=True, default="")


    order = models.PositiveIntegerField(
        "Порядок",
        default=0
    )

    class Meta:
        verbose_name = "Доп інформація"
        verbose_name_plural = "Доп інформація"

    
class PortfolioDetailsData(models.Model):

    p_data = models.ForeignKey(
    Portfolio,
    on_delete=models.CASCADE,
    related_name="data"
    )

    key = models.CharField("Параметр", max_length=100, blank=True, default="")
    feture = models.CharField("Значення", max_length=100, blank=True, default="")

    order = models.PositiveIntegerField(
        "Порядок",
        default=0
    )

    class Meta:
        verbose_name = "Тех інформація"
        verbose_name_plural = "Тех інформація"


class TechnicalDetails(models.Model):

    p_tech_details = models.ForeignKey(
    Portfolio,
    on_delete=models.CASCADE,
    related_name="document"
    )

    doc_name = models.CharField("Назва Проекту", max_length=100, blank=True, default="")
    slug = models.SlugField(unique=True)
    doc_content = HTMLField(
        "Технічна документація"
    )
    img_doc = models.ImageField(
        "Зображення документація",
        upload_to=upload_home_portfolio
    )
    img_doc_alt = models.CharField("Опис для зображення", max_length=300, blank=True)

    order = models.PositiveIntegerField(
        "Порядок",
        default=0
    )
    def save(self, *args, **kwargs):

        if not self.slug:
            base_slug = slugify(self.doc_name)
            slug = base_slug

            counter = 1
            while TechnicalDetails.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1

            self.slug = slug

        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Тех документація"
        verbose_name_plural = "Тех документація"


class PortfolioImage(models.Model):

    p_image = models.ForeignKey(
        Portfolio,
        on_delete=models.CASCADE,
        related_name="images",
        verbose_name="Блок фотогалерея"
    )

    image = models.ImageField(
        "Портфоліо фото",
        upload_to=upload_home_portfolio
    )

    alt_text = models.CharField(
        "Alt текст",
        max_length=255,
        blank=True
    )
    order = models.PositiveIntegerField(
        "Порядок",
        default=0
    )
    
    class Meta:
        ordering = ["order"]
        verbose_name = "Зображення"
        verbose_name_plural = "Зображення"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.image:
            compress_image(self.image.path, (1920, 900))

    def __str__(self):
        return f"Image"
    

class PortfolioPage(models.Model):
  
    h1 = models.CharField("Заголовок сторінки", max_length=200, blank=True, default="")

    class Meta:
        verbose_name = "Портфоліо сторінка"
        verbose_name_plural = "Портфоліо сторінка"

    def __str__(self):
        return "Портфоліо сторінка"