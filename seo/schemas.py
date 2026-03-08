def organization_schema(request):

    return {
        "@context": "https://schema.org",
        "@type": "Organization",
        "name": "Your Company",
        "url": request.build_absolute_uri("/"),
        "logo": request.build_absolute_uri("/static/logo.png")
    }