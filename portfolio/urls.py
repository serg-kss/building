from django.urls import path
from portfolio import views


app_name = 'portfolio'

urlpatterns = [
    path("portfolio", views.portfolio, name="portfolio"),
    path("portfolio/portfolio-details", views.portfolio_details, name="portfolio-details"),
]