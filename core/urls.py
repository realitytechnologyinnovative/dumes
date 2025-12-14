"""
URL configuration for core app
"""
from django.urls import path
from . import views

urlpatterns = [
    # Main pages
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('projects/', views.projects, name='projects'),
    path('contact/', views.contact, name='contact'),
    path('amenities/', views.amenities, name='amenities'),
    path('housing-types/', views.housing_types, name='housing_types'),
    path('housing-types-3-cols/', views.housing_types_3_cols, name='housing_types_3_cols'),
    
    # Project detail pages
    path('projects/luxury-service-apartment/', views.luxury_service_apartment, name='luxury_service_apartment'),
    path('projects/wuse-housing-scheme/', views.wuse_housing_scheme, name='wuse_housing_scheme'),
    path('projects/maitama-luxury-estate/', views.maitama_luxury_estate, name='maitama_luxury_estate'),
]


