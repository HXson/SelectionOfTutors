from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='main'),
    path('about', views.about, name='about'),
    path('create', views.create, name='create'),
    path('singIn', views.singIn, name='singIn'),
    path('registration', views.registration, name='registration'),
    
]