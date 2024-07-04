from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def carrito(request):
    return render(request, "cart_view.html")