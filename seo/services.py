from .models import PageSEO


def get_seo(page_key):

    seo = PageSEO.objects.filter(page=page_key).first()

    if seo:
        return seo

    return {
        "title": "Website",
        "description": "",
        "canonical": ""
    }