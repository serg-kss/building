from .models import ContactsData, SocialMedia


def site_settings(request):
    social = SocialMedia.objects.first()
    settings = ContactsData.objects.first()

    context = {
        "site_address": getattr(settings, "address", "") or "",
        "site_city": getattr(settings, "city", "") or "",
        "site_map": getattr(settings, "google_maps_url", "") or "",
        "site_phone": getattr(settings, "phone", "") or "",
        "site_email": getattr(settings, "email", "") or "",
        "site_instagram": getattr(social, "instagram", "") or "",
        "site_facebook": getattr(social, "facebook", "") or "",
        "site_twitter": getattr(social, "twitter", "") or "",
        "site_linkedin": getattr(social, "linkedin", "") or "",
        "site_youtube": getattr(social, "youtube", "") or ""
    }

    return context