"""
URL configuration for doja_galeria project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from galeria import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('galeria/', views.galeria, name='galeria'),
    path('artista/', views.artista, name='artista'),
    path('albuns/', views.albuns, name='albuns'),
    path('amala/', views.amala, name='amala'),
    path('hotpink/', views.hotpink, name='hotpink'),
    path('planether/', views.planether, name='planether'),
    path('scarlet/', views.scarlet, name='scarlet'),
    path('stream/', views.stream, name='stream'),
    path('criadores/', views.criadores, name='criadores'),
]
