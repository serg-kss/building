from django.urls import path
from main import views
from .views import Contact, Home, About


app_name = 'main'

urlpatterns = [
    path("", Home.as_view(), name="index"),
    path("contact", Contact.as_view(), name="contact"),
    path("about", About.as_view(), name="about"),
]