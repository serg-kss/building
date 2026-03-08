from .services import get_seo


def seo(request):

    path = request.path.strip("/")

    if not path:
        page = "home"
    else:
        page = path.split("/")[0]

    seo = get_seo(page)

    return {
        "seo": seo
    }