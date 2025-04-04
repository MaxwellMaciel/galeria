from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sobre/', views.sobre, name='sobre'),
    path('albuns/', views.albuns, name='albuns'),
    path('galeria/', views.galeria, name='galeria'),
    path('ouvir/', views.ouvir, name='ouvir'),
] 