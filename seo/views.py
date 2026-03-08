from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def robots(request):

    content = """
User-agent: *
Allow: /

Sitemap: https://example.com/sitemap.xml
"""

    return HttpResponse(content, content_type="text/plain")