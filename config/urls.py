from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from seo.views import robots


urlpatterns = [
    path("admin/", admin.site.urls),

    path("", include(("main.urls", "main"), namespace="main")),
    path("", include(("services.urls", "services"), namespace="services")),
    path("", include(("portfolio.urls", "portfolio"), namespace="portfolio")),

    path("cookies/", include("cookie_consent.urls")),
    path("robots.txt", robots),

    path("tinymce/", include("tinymce.urls")),
]


# MEDIA только через static()
urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)