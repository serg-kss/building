from django.views.generic import ListView, DetailView, View
from portfolio.models import Portfolio, PortfolioPage, TechnicalDetails
from django.shortcuts import render


class PortfolioView(View):

    def get(self, request):

        portfolio_list = Portfolio.objects.all()
        settings = PortfolioPage.objects.first()

        context = {
            "title_h1": settings.h1 if settings else "",
            "breadcrumbs": "Наші проекти",
            "portfolio_list": portfolio_list,
        }

        return render(request, "portfolio/portfolio.html", context)



class PortfolioDetailView(DetailView):

    model = Portfolio
    template_name = "portfolio/portfolio-details.html"
    context_object_name = "portfolio"
    slug_field = "slug"
    slug_url_kwarg = "slug"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context["title_h1"] = self.object.name
        context["breadcrumbs"] = "Портфоліо"
        return context


class PortfolioDocumentDetailView(DetailView):

    model = TechnicalDetails
    template_name = "portfolio/document.html"
    context_object_name = "document"
    slug_field = "slug"
    slug_url_kwarg = "slug"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context["title_h1"] = self.object.doc_name
        context["breadcrumbs"] = "Портфоліо"
        return context
  