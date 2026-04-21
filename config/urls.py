from django.contrib import admin
from django.urls import include, path, re_path
from django.conf import settings
from django.views.static import serve

from seo.views import robots


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(("main.urls", "main"), namespace="main")),
    path("", include(("services.urls", "services"), namespace="services")),
    path("", include(("portfolio.urls", "portfolio"), namespace="portfolio")),
    path("cookies/", include("cookie_consent.urls")),
    path("robots.txt", robots)
]

urlpatterns += [
    path("tinymce/", include("tinymce.urls")),
]

# 🔥 КОСТЫЛЬ ДЛЯ MEDIA (в самом конце!)
urlpatterns += [
    re_path(r"^media/(?P<path>.*)$", serve, {
        "document_root": settings.MEDIA_ROOT,
    }),
]