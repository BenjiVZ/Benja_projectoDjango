from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def catalogo_admin(request):
    return render(request, "admin.html")