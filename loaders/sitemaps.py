# myapp/sitemaps.py
from django.contrib.sitemaps import Sitemap
from .models import Loader

class LoaderSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        # Bosh sahifa + unique group_id lar
        group_ids = list(Loader.objects.values_list('group_id', flat=True).distinct())
        return [''] + group_ids  # '' -> bosh sahifa /  

    def location(self, item):
        # item bo'sh string bo'lsa bosh sahifa, aks holda group_id
        if item == '':
            return '/'  # bosh sahifa
        return f'/{item}/'
