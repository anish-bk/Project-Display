"""
URL Configuration for the Project Showcase App

Defines all URL patterns for the promotional website pages.
"""

from django.urls import path
from . import views

app_name = 'project_showcase'

urlpatterns = [
    # Main pages
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('technology/', views.technology, name='technology'),
    path('architecture/', views.architecture, name='architecture'),
    path('features/', views.features, name='features'),
    path('screenshots/', views.screenshots, name='screenshots'),
    path('results/', views.results, name='results'),
    path('future-scope/', views.future_scope, name='future_scope'),
    path('contact/', views.contact, name='contact'),
    path('team/', views.team, name='team'),
        path('virtual-museum/', views.virtual_museum, name='virtual_museum'),
    
    # AJAX endpoints
    path('contact/submit/', views.contact_submit, name='contact_submit'),
]
