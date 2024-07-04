from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from app_admin.models import Producto

# Create your views here.
@login_required

def menu1(request):
    # Lógica para menu1
    return render(request, 'menu1.html')

def menu2(request):
    # Lógica para menu2
    return render(request, 'menu2.html')


""" def page_1(request):
    context = {
        "user": request.user,
    }
    return render(request, "index.html", context) """

""" def page_1(request):
    productos_tendencia = Producto.objects.filter(tendencia=True)
    data = {
        'productos': productos_tendencia
    }
    return render(request, "index.html", data) """

def page_1(request):
    productos_tendencia = Producto.objects.filter(tendencia=True)
    productos_populares = Producto.objects.filter(popular=True)
    data = {
        'tendencia': productos_tendencia,
        'populares': productos_populares
    }
    return render(request, "index.html", data)


""" def page_populares(request):
    productos_populares = Producto.objects.filter(popular=True)
    data = {
        'productos': productos_populares
    }
    return render(request, "articulo.html", data) """
