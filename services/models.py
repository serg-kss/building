from django.db import models
from tinymce.models import HTMLField
from django.utils.text import slugify
from main.utils.image import compress_image
from tinymce.models import HTMLField


class ServicePage(models.Model):

    h1 = models.CharField("Заголовок сторінки", max_length=200, blank=False, default="Services")
    sub_title = models.CharField("Заголовок сторінки", max_length=200, blank=True, default="Additional Services")
    sub_text = models.TextField("Доп текст", max_length=500, blank=True, default="")
    img_main = models.ImageField(
        "Зображення",
        upload_to="service/"
    )
    img_main_alt = models.CharField("Опис для зображення", max_length=300, blank=True)


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.img_main:
            compress_image(self.img_main.path, (1920, 900))

    class Meta:
        verbose_name = "Послуги сторінка"
        verbose_name_plural = "Послуги сторінка"

    def __str__(self):
        return "Послуги сторінка"


class ServicePageExtraServices(models.Model):

    page = models.ForeignKey(
    ServicePage,
    on_delete=models.CASCADE,
    related_name="extra",
    verbose_name="Доп послуга"
    )

    option_title = models.CharField("Заголовок", max_length=200, blank=False, default="Services")
    option_text = models.CharField("Текст", max_length=200, blank=False, default="Services")
    order = models.PositiveIntegerField(
        "Порядок",
        default=0
    )
    
    class Meta:
        ordering = ["order"]
        verbose_name = "Доп послуга"
        verbose_name_plural = "Доп послуги"

    def __str__(self):
        return f"Image"


class Service(models.Model):
    name = models.CharField("Назва Сервісу", max_length=100)
    slug = models.SlugField(unique=True, blank=False)
    sub_text = models.TextField("Доп текст", max_length=500, blank=True, default="")
    option_1 = models.CharField("Доп інфо 1", max_length=100)
    option_2 = models.CharField("Доп інфо 2", max_length=100)
    option_3 = models.CharField("Доп інфо 3", max_length=100)


    content = HTMLField(
        "Опис проекту"
    )
    img_main = models.ImageField(
        "Зображення",
        upload_to="service/"
    )
    img_main_alt = models.CharField("Опис для зображення", max_length=300, blank=True)
    title = models.CharField("Назва сервісу", max_length=200, blank=True, default="")
    text = models.TextField("Доп текст", max_length=500, blank=True, default="")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
        if self.img_main:
            compress_image(self.img_main.path, (1920, 900))

    class Meta:
        verbose_name = "Сервіс"
        verbose_name_plural = "Сервіси"

    def __str__(self):
        return f"{self.name}"
    

class ServiceDetailsData(models.Model):

    s_data = models.ForeignKey(
    Service,
    on_delete=models.CASCADE,
    related_name="data"
    )

    key = models.CharField("Параметр", max_length=100, blank=False, default="")
    feture = models.CharField("Значення", max_length=100, blank=False, default="")

    order = models.PositiveIntegerField(
        "Порядок",
        default=0
    )

    class Meta:
        verbose_name = "Доп інформація"
        verbose_name_plural = "Доп інформація"


class ServiceMethodology(models.Model):

    methodology = models.ForeignKey(
    Service,
    on_delete=models.CASCADE,
    related_name="methodology"
    )

    title = models.CharField("Назва", max_length=200, blank=True, default="")
    text = models.TextField("Інформація", max_length=500, blank=True, default="")
    option_1 = models.CharField("Доп інфо 1", max_length=200)
    option_2 = models.CharField("Доп інфо 2", max_length=200)
    option_3 = models.CharField("Доп інфо 3", max_length=200)

    order = models.PositiveIntegerField(
        "Порядок",
        default=0
    )

    class Meta:
        verbose_name = "Методологія"
        verbose_name_plural = "Методологіі"


class ServiceCapabilities(models.Model):

    сapabilities = models.ForeignKey(
    Service,
    on_delete=models.CASCADE,
    related_name="сapabilities"
    )
        
    title = models.CharField("Назва", max_length=200, blank=True, default="")
    text = models.TextField("Інформація", max_length=500, blank=True, default="")

    order = models.PositiveIntegerField(
        "Порядок",
        default=0
    )

    class Meta:
        verbose_name = "Можливість"
        verbose_name_plural = "Можливості"