from django.db import models
from main.utils.image import compress_image
from tinymce.models import HTMLField
    
    
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
        verbose_name_plural = "Контакти"


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

    h1 = models.CharField("Вступ: H1 заголовок", max_length=255)
    hero_text = models.TextField("Вступ: Текст під заголовком H1")
    hero_years_experience = models.CharField("Вступ: Роки на ринку", max_length=10)
    hero_projects_completed = models.CharField("Вступ: Завершено проектів", max_length=10)
    hero_satisfied_clients = models.CharField("Вступ: Кількість клієнтів", max_length=10)
    hero_img = models.ImageField("Вступ: Зображення (1920 × 1080)", upload_to="home_main/")
    hero_img_alt = models.CharField("Вступ: Зображення - опис (alt)", max_length=300)
    hero_video = models.URLField("Ютуб посилання")

    sub_title_services = models.CharField("Послуги: Заголовок розділу", max_length=255)
    sub_text_services = models.CharField("Послуги: Доп текст розділу", max_length=500)

    sub_title_portfolio = models.CharField("Проекти: Заголовок розділу", max_length=255)
    sub_text_portfolio = models.CharField("Проекти: Доп текст розділу", max_length=500)

    sub_title_certif = models.CharField("Сертифікати: Заголовок розділу", max_length=255)
    sub_text_certif = models.CharField("Сертифікати: Доп текст розділу", max_length=500)
    title_certif = models.CharField("Сертифікати: Заголовок", max_length=255)
    text_certif = models.TextField("Сертифікати: Текст")
    img_certif = models.ImageField("Сертифікати: Зображення (1920 × 1080)", upload_to="home_main/")
    img_certif_alt = models.CharField("Сертифікати: Зображення - опис (alt)", max_length=300)
    title_certif_img = models.CharField("Сертифікати: Заголовок блок з зображенням", max_length=255)
    text_certif_img = models.TextField("Сертифікати: Текст блок з зображенням")
    awards_certif = models.CharField("Сертифікати: Кількість")

    sub_title_team = models.CharField("Команда: Заголовок розділу", max_length=255)
    sub_text_team = models.CharField("Команда: Доп текст розділу", max_length=500)

    title_quote = models.CharField("Підтримка: Заголовок", max_length=255)
    text_quote = models.TextField("Підтримка: Текст")
    option_1 = models.CharField("Підтримка: доп 1", max_length=255, blank=True)
    option_2 = models.CharField("Підтримка: доп 2", max_length=255, blank=True)
    option_3 = models.CharField("Підтримка: доп 3", max_length=255, blank=True)


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.hero_img:
            compress_image(self.hero_img.path, (1920, 900))

        if self.img_certif:
            compress_image(self.img_certif.path, (1920, 900))

    class Meta:
        verbose_name = "Головну сторінку"
        verbose_name_plural = "Головна"

    def __str__(self):
        return "Таблиця для редагування інформації на головній сторінці сайту"


class HomePageCertifCreator(models.Model):
    about = models.ForeignKey(
    HomePage,
    on_delete=models.CASCADE,
    related_name="certif",
    verbose_name="Блок Добавити Сертифікат"
    )

    title = models.CharField("Назва сертифікату", max_length=255)
    sub_title = models.CharField("Доп інформація", max_length=255)
    text = models.TextField("Опис", max_length=600)
    img = models.ImageField(
        "Зображення сертифікату",
        upload_to="home_about/",
        null=True
    )
    alt_img = models.CharField(
        "Alt текст для зображення",
        max_length=255,
        blank=True,
        null=True,
    )
    order = models.PositiveIntegerField(
        "Порядок",
        default=0
    )
    
    class Meta:
        ordering = ["order"]
        verbose_name = "Сертифікат"
        verbose_name_plural = "Сертифікати"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.img:
            compress_image(self.img.path, (1920, 900))


class AboutPage(models.Model):

    h1_about = models.CharField("H1 сторінка про компанію", max_length=255)
    h1_team = models.CharField("H1 сторінка команда", max_length=255)

    h2 = models.CharField("Історія заголовок", max_length=255)
    history_text = HTMLField("Історія Компанії")
    history_img_left = models.ImageField(
        "Зображення (left)",
        upload_to="home_about/",
         null=True
    )
    alt_img_left = models.CharField(
        "Alt текст (left)",
        max_length=255,
        blank=True,
        null=True,
    )
    history_img_right = models.ImageField(
        "Зображення (right)",
        upload_to="home_about/",
         null=True,
    )
    alt_img_right = models.CharField(
        "Alt текст (right)",
        max_length=255,
        blank=True,
         null=True
    )
    history_video = models.URLField("Ютуб посилання", blank=True)

    years_number_statistics = models.PositiveIntegerField("Кількість років", blank=True, null=True, default=0)
    projects_number_statistics = models.PositiveIntegerField("Кількість Проектів", blank=True, null=True, default=0)
    workers_number_statistics = models.PositiveIntegerField("Кількість працівників", blank=True, null=True, default=0)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.history_img_left:
            compress_image(self.history_img_left.path, (1920, 900))
        if self.history_img_right:
            compress_image(self.history_img_right.path, (1920, 900))

    class Meta:
        verbose_name = "Сторінку про компанію"
        verbose_name_plural = "Про компанію"

    def __str__(self):
        return "Сторінка про компанію"

    def save(self, *args, **kwargs):
        if not self.pk and AboutPage.objects.exists():
            raise ValueError("Може бути тільки одна сторінка")
        return super().save(*args, **kwargs)    
    

class AboutImage(models.Model):

    about = models.ForeignKey(
        AboutPage,
        on_delete=models.CASCADE,
        related_name="images",
        verbose_name="Блок About"
    )

    image = models.ImageField(
        "Зображення сертифікатів",
        upload_to="home_about/"
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
        ordering = ["order"]   # ⭐ ВОТ ЭТО НУЖНО
        verbose_name = "Зображення"
        verbose_name_plural = "Зображення"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.image:
            compress_image(self.image.path, (1920, 900))

    def __str__(self):
        return f"Image for {self.about}"


class TeamAboutPage(models.Model):

    page = models.ForeignKey(
        AboutPage,
        on_delete=models.CASCADE,
        related_name="team"
    )

    team_name = models.CharField("Імʼя", max_length=150)
    team_position = models.CharField("Посада", max_length=150)
    team_description = models.CharField("Детальна інформація", max_length=350, blank=True)
    email = models.EmailField("Email", max_length=254, blank=True)
    linkedin = models.URLField("linkedin", blank=True)
    phone = models.CharField("Телефон", max_length=15)
    option_1 = models.CharField("Доп інфо 1", max_length=50, blank=True)
    option_2 = models.CharField("Доп інфо 2", max_length=50, blank=True)
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
    testimonials_company = models.CharField("Компанія", max_length=150)
    testimonials_message = models.TextField("Відгук")
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
    

class Terms(models.Model):

    h1 = models.CharField("H1 заголовок", max_length=255)

    content = HTMLField(
        "Опис проекту"
    )

    class Meta:
        verbose_name = "Умови обслуговування"
        verbose_name_plural = "Сторінка умови"

    def __str__(self):
        return f"{self.h1}"
    

class Privacy(models.Model):

    h1 = models.CharField("H1 заголовок", max_length=255)

    content = HTMLField(
        "Опис проекту"
    )

    class Meta:
        verbose_name = "Політика конфіденційності"
        verbose_name_plural = "Конфіденційність"

    def __str__(self):
        return f"{self.h1}"
    

class Gallery(models.Model):

    title = models.CharField("Заголовок", max_length=255, default="")
    text = models.CharField("Опис", max_length=500, default="")

    img = models.ImageField(
        "Фото - галерея",
        upload_to="home_gallery/"
    )
    alt_img = models.CharField(
        "Alt текст",
        max_length=255,
        blank=True,
        null=True
    )
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.img:
            compress_image(self.img.path, (1920, 900))

    class Meta:
        verbose_name = "Фото галерея"
        verbose_name_plural = "Фото галерея"

    def __str__(self):
        return f"{self.alt_img}"
