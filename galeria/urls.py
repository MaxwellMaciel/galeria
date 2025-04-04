from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sobre/', views.sobre, name='sobre'),
    path('albuns/', views.albuns, name='albuns'),
    path('galeria/', views.galeria, name='galeria'),
    path('ouvir/', views.ouvir, name='ouvir'),
    path('albuns/amala/', views.amala, name='amala'),
    path('albuns/hotpink/', views.hotpink, name='hotpink'),
    path('albuns/planether/', views.planether, name='planether'),
    path('albuns/scarlet/', views.scarlet, name='scarlet'),
] 