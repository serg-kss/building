from django.shortcuts import render
from django.views import View
from django.http import JsonResponse

from main.models import ContactMessages, HomePage

class Home(View):

    def get(self, request):

        page = HomePage.objects.first()
        slides = page.slides.all() if page else []

        context = {
            "page": page,
            "slides": slides,
        }

        return render(request, "main/index.html", context)


    def post(self, request):

        # обработка формы
        name = request.POST.get("name")

        ...

        return JsonResponse({"status": "success"})


class Contact(View):

    def get(self, request):
        return render(
            request,
            "main/contact.html",
            {
                "title_h1": "Контакти",
                "breadcrumbs": "Контакти",
            },
        )

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

        #page = HomePageSeo.objects.first()
        #slides = page.slides.all()

        context = {
            "title_h1": "Про компанію",
            "breadcrumbs": "Про компанію",
        }

        return render(request, "main/about.html", context)
