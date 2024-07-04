from django.shortcuts import render
from django.http import HttpResponse
from app_admin.models import Producto

# Create your views here.

def catalogo(request):
    productos = Producto.objects.all()
    data = {
        'productos': productos
    }
    return render(request, "catalogo.html", data)