from django.db import models
from tinymce.models import HTMLField
from django.utils.text import slugify


class Service(models.Model):
    name = models.CharField("Назва Сервісу", max_length=100)
    content = HTMLField(
        "Опис сервісу"
    )

    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Сервіс"
        verbose_name_plural = "Сервіси"

    def __str__(self):
        return f"{self.name}"
