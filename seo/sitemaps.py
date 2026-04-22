from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from services.models import Service
from portfolio.models import Portfolio


class StaticSitemap(Sitemap):

    priority = 0.8
    changefreq = "weekly"

    def items(self):
        return [
            "main:index",
            "main:services",
            "main:portfolio",
            "main:contact",
        ]

    def location(self, item):
        return reverse(item)


class ServiceSitemap(Sitemap):

    changefreq = "weekly"

    def items(self):
        return Service.objects.all()

    def location(self, obj):
        return obj.get_absolute_url()

    def priority(self, obj):
        if obj.seo:
            return obj.seo.priority
        return 0.7


class PortfolioSitemap(Sitemap):

    changefreq = "weekly"

    def items(self):
        return Portfolio.objects.all()

    def location(self, obj):
        return obj.get_absolute_url()

    def priority(self, obj):
        if obj.seo:
            return obj.seo.priority
        return 0.7