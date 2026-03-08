from django.urls import path
from services import views


app_name = 'services'

urlpatterns = [
    path("services/", views.ServicesView.as_view(), name="services"),
    path("services/<slug:slug>/", views.ServiceDetailView.as_view(), name="service"),
]