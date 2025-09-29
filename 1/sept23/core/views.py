from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.

def home(request):
    titulo = "Inicio"

    productos = ['computadores', 'perifericos', 'servidores']

    data = {
        "titulo": titulo,
        "productos":productos
    }
    return render(request, 'core/home.html', data)

def contacto(request):
    return render(request, 'core/contacto.html')