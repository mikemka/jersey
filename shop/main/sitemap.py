from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class MainSitemap(Sitemap):
    changefreq = "weekly"
    priority = 1

    def items(self):
        return ('homepage',)
    
    def location(self, item):
        return reverse(item)
