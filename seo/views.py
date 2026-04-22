from django.http import HttpResponse


def robots(request):

    sitemap_url = request.build_absolute_uri(
        "/sitemap.xml"
    )

    content = f"""
User-agent: *
Allow: /

Sitemap: {sitemap_url}
"""

    return HttpResponse(
        content,
        content_type="text/plain"
    )