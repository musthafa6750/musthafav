from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Default home page
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('resume/', views.resume, name='resume'),
    path('projects/', views.projects, name='projects'),
   
   
]