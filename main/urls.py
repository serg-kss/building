from django.urls import path
from .views import Contact, Gallery, Home, About, Privacy, Quote, Team, Terms


app_name = 'main'

urlpatterns = [
    path("", Home.as_view(), name="index"),
    path("contact", Contact.as_view(), name="contact"),
    path("about", About.as_view(), name="about"),
    path("team", Team.as_view(), name="team"),
    path("quote", Quote.as_view(), name="quote"),
    path("terms", Terms.as_view(), name="terms"),
    path("privacy", Privacy.as_view(), name="privacy"),
    path("gallery", Gallery.as_view(), name="gallery"),
]