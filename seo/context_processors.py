from .services import get_seo
import json

def seo(request):

    path = request.path.strip("/")

    seo_object = get_seo(path)

    return {
        "seo": seo_object
    }


def organization_schema(request):

    schema = {
        "@context": "https://schema.org",
        "@type": "Organization",

        "name": "Білдінг Естейт",

        "url": request.build_absolute_uri("/"),

        "logo": request.build_absolute_uri(
            "/static/assets/img/logo.jpg"
        ),
    }

    return {
        "organization_schema": json.dumps(
            schema,
            ensure_ascii=False
        )
    }