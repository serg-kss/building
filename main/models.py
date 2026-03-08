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

    twitter = models.URLField("Twitter (X)", max_length=150, blank=True, default="")
    instagram = models.URLField("Instagram", max_length=150, blank=True, default="")
    facebook = models.URLField("Facebook", max_length=150, blank=True, default="")
    linkedin = models.URLField("Linked In", max_length=150, blank=True, default="")
    youtube = models.URLField("YouTube", max_length=200, blank=True, default="")

    def __str__(self):
        return "Таблиця зі списком доступних для редагування соціальних мереж"

    class Meta:
        verbose_name = "Соціальні мережі"
        verbose_name_plural = "Соціальні мережі"


class HomePage(models.Model):

    h1 = models.CharField("H1 заголовок", max_length=255)

    class Meta:
        verbose_name = "Головну сторінку"
        verbose_name_plural = "Головна сторінка"

    def __str__(self):
        return "Таблиця для редагування інформації на головній сторінці сайту"

    def save(self, *args, **kwargs):
        if not self.pk and HomePage.objects.exists():
            raise ValueError("Може бути тільки одна головна сторінка")
        return super().save(*args, **kwargs)


class HomeSlider(models.Model):

    page = models.ForeignKey(
        HomePage,
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
    

class AboutPage(models.Model):

    h1 = models.CharField("H1 заголовок", max_length=255)

    h2 = models.CharField("Історія заголовок", max_length=255)
    history_text = models.TextField("Історія Компанії", blank=True, default='')
    history_img = models.ImageField(
        "Зображення",
        upload_to="home_about/"
    )
    history_video = models.URLField("Ютуб посилання", blank=True)

    title_statistics = models.CharField("Заголовок", max_length=255, blank=True)
    subtitle_statistics = models.CharField("Підзаголовок", max_length=255, blank=True)
    clients_number_statistics = models.PositiveIntegerField("Клієнти", blank=True, default=10)
    projects_number_statistics = models.PositiveIntegerField("Проекти", blank=True, default=10)
    support_h_number_statistics = models.PositiveIntegerField("Години підтримки", blank=True, default=100)
    workers_number_statistics = models.PositiveIntegerField("Робітник", blank=True, default=100)
    statistics_img = models.ImageField(
        "Зображення перше",
        upload_to="home_about/"
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.history_img:
            compress_image(self.history_img.path, (1920, 900))

    class Meta:
        verbose_name = "Сторінку про компанію"
        verbose_name_plural = "Сторінка про компанію"

    def __str__(self):
        return "Сторінка про компанію"

    def save(self, *args, **kwargs):
        if not self.pk and AboutPage.objects.exists():
            raise ValueError("Може бути тільки одна сторінка")
        return super().save(*args, **kwargs)    


class TeamAboutPage(models.Model):

    page = models.ForeignKey(
        AboutPage,
        on_delete=models.CASCADE,
        related_name="team"
    )

    team_name = models.CharField("Імʼя", max_length=150)
    team_position = models.CharField("Посада", max_length=150)
    team_description = models.CharField("Детальна інформація", max_length=350)
    twitter = models.URLField("twitter", blank=True)
    facebook = models.URLField("facebook", blank=True)
    instagram = models.URLField("instagram", blank=True)
    linkedin = models.URLField("linkedin", blank=True)
    team_img = models.ImageField(
        "Зображення",
        upload_to="home_about_team/"
    )
    order = models.PositiveIntegerField(
        "Порядок",
        default=0
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.team_img:
            compress_image(self.team_img.path, (1920, 900))

    class Meta:
        verbose_name = "Учасник команди"
        verbose_name_plural = "Учасники команди"

    def __str__(self):
        return f"{self.order} {self.team_name}"
    
class TestimonialsAboutPage(models.Model):

    page = models.ForeignKey(
        AboutPage,
        on_delete=models.CASCADE,
        related_name="testimonials"
    )

    testimonials_name = models.CharField("Імʼя", max_length=150)
    testimonials_position = models.CharField("Посада", max_length=150)
    testimonials_message = models.CharField("Відгук")
    testimonials_img = models.ImageField(
        "Аватар",
        upload_to="home_about_testimonials/"
    )
    order = models.PositiveIntegerField(
        "Порядок",
        default=0
    )
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.testimonials_img:
            compress_image(self.testimonials_img.path, (1920, 900))

    class Meta:
        verbose_name = "Відгук"
        verbose_name_plural = "Відгуки"

    def __str__(self):
        return f"{self.order} {self.testimonials_name}"