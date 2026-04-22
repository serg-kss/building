from .models import PageSEO


def get_seo(path):

    # Главная страница
    if not path:
        return PageSEO.objects.filter(
            page="home"
        ).first()

    parts = path.split("/")

    page = parts[0]

    slug = None

    if len(parts) > 1:
        slug = parts[1]

    # Сначала ищем по slug
    if slug:
        seo = PageSEO.objects.filter(
            slug=slug
        ).first()

        if seo:
            return seo

    # Потом fallback на page
    return PageSEO.objects.filter(
        page=page
    ).first()