from django.urls import path
from blog import views


app_name = 'blog'

urlpatterns = [
    path("blog", views.blog, name="blog"),
    path("blog/blog-details", views.blog_details, name="blog-details"),
]