from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'galeria/index.html')

def galeria(request):
    return render(request, 'galeria/galeria.html')

def artista(request):
    return render(request, 'galeria/artista.html')

def albuns(request):
    return render(request, 'galeria/albuns.html')

def amala(request):
    return render(request, 'galeria/amala.html')

def hotpink(request):
    return render(request, 'galeria/hotpink.html')

def planether(request):
    return render(request, 'galeria/planether.html')

def scarlet(request):
    return render(request, 'galeria/scarlet.html')

def stream(request):
    return render(request, 'galeria/stream.html')
