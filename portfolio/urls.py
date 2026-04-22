from django.urls import path
from portfolio import views


app_name = 'portfolio'

urlpatterns = [
    path("portfolio/", views.PortfolioView.as_view(), name="portfolio"),
    path("portfolio/<slug:slug>/", views.PortfolioDetailView.as_view(), name="portfolio-details"),
    path("portfolio/documents/<slug:slug>/", views.PortfolioDocumentDetailView.as_view(), name="document"),
]