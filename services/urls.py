from django.urls import path
from services import views


app_name = 'services'

urlpatterns = [
    path("services", views.services, name="services"),
]