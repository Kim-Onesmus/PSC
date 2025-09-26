from django.urls import path
from . import views
from app.sitemap import StaticSitemap
from django.views.generic.base import TemplateView
from django.contrib.sitemaps.views import sitemap

sitemaps = {
    'static': StaticSitemap,
}

urlpatterns = [
    path('', views.Index, name='index'),
    path('sitemap.xml', sitemap, {'sitemaps':sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('robots.txt', TemplateView.as_view(template_name="app/robots.txt", content_type="text/plain")),
    path('about', views.About, name='about'),
    path('core_values', views.CoreValues, name='core_values'),
    path('areas_of_interests', views.AreasofInterests, name='areas_of_interests'),
    path('why_us', views.WhyUs, name='why_us'),
    path('contact', views.Contact, name='contact'),
    path('leadership', views.Leadership, name='leadership'),
]