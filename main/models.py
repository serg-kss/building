from django.db import models

from main.utils.image import compress_image
    
class ContactMessages(models.Model):

    name = models.CharField("Імʼя клієнта", max_length=20)
    email = models.EmailField("Email")
    subject = models.CharField("Тема", max_length=200)
    message = models.TextField("Повідомлення")

    created_at = models.DateTimeField(
        "Дата повідомлення",
        auto_now_add=True
    )

    is_read = models.BooleanField("Прочитано", default=False)

    def __str__(self):
        return self.subject
    
    class Meta:
        verbose_name = "Повідомлення"
        verbose_name_plural = "Повідомлення"
        ordering = ["-created_at"]


class ContactsData(models.Model):

    address = models.TextField("Адреса", blank=True)

    city = models.TextField("Місто, Область, Поштовий індекс", blank=True)

    phone = models.CharField("Номер телефону", max_length=50, blank=True)
    email = models.EmailField("Email адреса", blank=True)

    google_maps_url = models.TextField("Google Maps посилання", blank=True)

    def __str__(self):
        return "Контактна інформація на сайті"

    class Meta:
        verbose_name = "Контактну інформацію"
        verbose_name_plural = "Контактна інформація"


class SocialMedia(models.Model):

    twitter = models.CharField("Twitter (X)", max_length=150, blank=True, default="")
    instagram = models.CharField("Instagram", max_length=150, blank=True, default="")
    facebook = models.CharField("Facebook", max_length=150, blank=True, default="")
    linkedin = models.CharField("Linked In", max_length=150, blank=True, default="")
    youtube = models.CharField("YouTube", max_length=200, blank=True, default="")

    def __str__(self):
        return "Соц-мережі"

    class Meta:
        verbose_name = "Соц-мережі"
        verbose_name_plural = "Соц-мережі"


from django.db import models


class HomePageSeo(models.Model):

    title = models.CharField("SEO: Title сторінки", max_length=255)
    description = models.TextField("SEO: Meta description", blank=True)
    h1 = models.CharField("H1 заголовок", max_length=255)

    class Meta:
        verbose_name = "Головну сторінку"
        verbose_name_plural = "Головна сторінка"

    def __str__(self):
        return "Головна сторінка"

    def save(self, *args, **kwargs):
        if not self.pk and HomePageSeo.objects.exists():
            raise ValueError("Може бути тільки одна головна сторінка")
        return super().save(*args, **kwargs)


class HomeSlider(models.Model):

    page = models.ForeignKey(
        HomePageSeo,
        on_delete=models.CASCADE,
        related_name="slides"
    )

    image = models.ImageField(
        "Фото слайду",
        upload_to="home_slider/"
    )

    image_mobile = models.ImageField(
        "Фото слайду (mobile)",
        upload_to="home_slider/",
        blank=True,
        null=True
    )

    order = models.PositiveIntegerField(
        "Порядок",
        default=0
    )

    alt = models.CharField("Alt", max_length=300)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.image:
            compress_image(self.image.path, (1920, 900))

        if self.image_mobile:
            compress_image(self.image_mobile.path, (768, 1200))

    class Meta:
        verbose_name = "Слайд"
        verbose_name_plural = "Слайдер головної сторінки"
        ordering = ["order"]

    def __str__(self):
        return f" {self.order}"