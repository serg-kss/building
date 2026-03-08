from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class StaticSitemap(Sitemap):

    def items(self):
        return [
            "main:index",
            "main:services",
            "main:portfolio",
            "main:contact"
        ]

    def location(self, item):
        return reverse(item)
    
class BlogSitemap(Sitemap):

    changefreq = "weekly"
    priority = 0.8

    def items(self):
        from blog.models import Post
        return Post.objects.filter(is_published=True)

    def location(self, obj):
        return obj.get_absolute_url()