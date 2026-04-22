from django.shortcuts import render
from django.views.generic import View, DetailView

from seo.models import PageSEO
from .models import Service, ServicePage


class ServicesView(View):

    def get(self, request):

        services_list = Service.objects.all()
        settings = ServicePage.objects.first()

        context = {
            "title_h1": settings.h1 if settings else "",
            "breadcrumbs": "Наші послуги",
            "services_list": services_list,
            "settings": settings,
        }

        return render(request, "services/services.html", context)



class ServiceDetailView(DetailView):

    model = Service
    template_name = "services/service.html"
    context_object_name = "service"
    slug_field = "slug"
    slug_url_kwarg = "slug"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        service = self.object
        context["title_h1"] = self.object.name
        context["breadcrumbs"] = "Сервіси"
        context["seo"] = (
            service.seo
            or PageSEO.objects.filter(page="services").first()
        )

        return context