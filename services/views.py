from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Service


class ServicesView(ListView):

    model = Service
    template_name = "services/services.html"
    context_object_name = "services"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context["title_h1"] = "Наші сервіси"
        context["breadcrumbs"] = "Сервіси"
        return context    



class ServiceDetailView(DetailView):

    model = Service
    template_name = "services/service.html"
    context_object_name = "service"
    slug_field = "slug"
    slug_url_kwarg = "slug"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context["title_h1"] = self.object.name
        context["breadcrumbs"] = "Сервіси"
        return context