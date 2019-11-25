from django.shortcuts import render
from .models import Flor,Estado #importar el modelo

# Create your views here. crear los controladores
# para las paginas web
def home(request):
    return render(request,'core/home.html')
    # retorna la pagina renderizada

def galeria(request):
    return render(request, 'core/galeria.html')