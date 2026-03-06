from django.contrib import admin
from django.urls import include, path, re_path
from django.conf import settings
from django.views.static import serve


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(("main.urls", "main"), namespace="main")),
    path("", include(("blog.urls", "blog"), namespace="blog")),
    path("", include(("services.urls", "services"), namespace="services")),
    path("", include(("portfolio.urls", "portfolio"), namespace="portfolio")),
]

# 🔥 КОСТЫЛЬ ДЛЯ MEDIA (в самом конце!)
urlpatterns += [
    re_path(r"^media/(?P<path>.*)$", serve, {
        "document_root": settings.MEDIA_ROOT,
    }),
]