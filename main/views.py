from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from django.core.paginator import Paginator

from main.models import (
    AboutPage,
    ContactMessages,
    HomePage,
    Terms as T,
    Privacy as P,
    Gallery as G,
)

from portfolio.models import Portfolio
from services.models import Service


class Home(View):

    def get(self, request):

        page = HomePage.objects.first()
        about = AboutPage.objects.first()

        services = Service.objects.all()
        portfolio = Portfolio.objects.all()

        testimonials = []
        team = []

        if about:
            testimonials = about.testimonials.all()
            team = about.team.all()

        context = {
            "page": page,
            "services": services,
            "portfolio": portfolio,
            "testimonials": testimonials,
            "team": team,
        }

        return render(request, "main/index.html", context)

    def post(self, request):

        name = request.POST.get("name")

        # ... твоя логика формы

        return JsonResponse({"status": "success"})


class Contact(View):

    def get(self, request):

        context = {
            "title_h1": "Контакти",
            "breadcrumbs": "Контакти",
        }

        return render(request, "main/contact.html", context)

    def post(self, request):

        # honeypot защита от ботов
        if request.POST.get("website"):
            return JsonResponse({"status": "error"})

        name = request.POST.get("name", "").strip()
        email = request.POST.get("email", "").strip()
        subject = request.POST.get("subject", "").strip()
        message = request.POST.get("message", "").strip()

        # проверка обязательных полей
        if not all([name, email, subject, message]):
            return JsonResponse(
                {"status": "error", "message": "Заповніть всі поля"},
                status=400,
            )

        # ограничение длины сообщения
        if len(message) > 1000:
            return JsonResponse(
                {"status": "error", "message": "Повідомлення занадто довге"},
                status=400,
            )

        ContactMessages.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message,
        )

        return JsonResponse({"status": "success"})


class About(View):

    def get(self, request):

        page = AboutPage.objects.first()

        certificates_img = []

        if page:
            certificates_img = page.images.all()

        context = {
            "title_h1": page.h1_about if page else "",
            "breadcrumbs": "Про компанію",
            "page": page,
            "certificates_img": certificates_img,
        }

        return render(request, "main/about.html", context)


class Team(View):

    def get(self, request):

        page = AboutPage.objects.first()

        team = []

        if page:
            team = page.team.all()

        context = {
            "title_h1": page.h1_team if page else "",
            "breadcrumbs": "Команда",
            "team": team,
        }

        return render(request, "main/team.html", context)


class Quote(View):

    def get(self, request):

        context = {
            "title_h1": "quote",
            "breadcrumbs": "quote",
        }

        return render(request, "main/quote.html", context)


class Terms(View):

    def get(self, request):

        page = T.objects.first()

        context = {
            "title_h1": page.h1 if page else "",
            "breadcrumbs": "Terms",
            "page": page,
        }

        return render(request, "main/terms.html", context)


class Privacy(View):

    def get(self, request):

        page = P.objects.first()

        context = {
            "title_h1": page.h1 if page else "",
            "breadcrumbs": "Privacy",
            "page": page,
        }

        return render(request, "main/privacy.html", context)


class Gallery(View):

    def get(self, request):

        photos_list = G.objects.all()

        paginator = Paginator(photos_list, 9)

        page_number = request.GET.get("page")

        photos = paginator.get_page(page_number)

        context = {
            "title_h1": "Галерея",
            "breadcrumbs": "Галерея",
            "photos": photos,
        }

        return render(request, "main/gallery.html", context)