from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index, name='index'),
    path('about', views.About, name='about'),
    path('core_values', views.CoreValues, name='core_values'),
    path('areas_of_interests', views.AreasofInterests, name='areas_of_interests'),
    path('why_us', views.WhyUs, name='why_us'),
    path('contact', views.Contact, name='contact'),
]