from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LoaderViewSet
from django.contrib.sitemaps.views import sitemap
from .sitemaps import LoaderSitemap

router = DefaultRouter()
router.register(r'loaders', LoaderViewSet, basename='loader')

sitemaps = {
    'loaders': LoaderSitemap,
}

urlpatterns = [
    path('', include(router.urls)),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
]
