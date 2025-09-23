from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'core/home.html')

def contacto(request):
    titulo = "<h1>contacto<h1/>"
    return HttpResponse(titulo)