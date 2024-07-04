from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RegistrationForm
from django.contrib.auth.views import LoginView

# Create your views here.
""" def log(request):
    return render(request, "login.html") """

""" def reg(request):
    return render(request, "register.html") """

""" def menu1(request):
    # Lógica para menu1
    return render(request, 'menu1.html')

def menu2(request):
    # Lógica para menu2
    return render(request, 'menu2.html')

from myapp.views import menu1,menu2 """

# views.py

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

""" def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if username == 'jojoto' and password == '1155':
                return redirect('catalogo_admin')
            return redirect('page')
        else:
            return render(request, 'login.html', {'error': 'Credenciales inválidas'})
    else:
        return render(request, 'login.html') """


from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Verifica si el usuario y la contraseña son los especiales
            if username == 'jojoto' and password == '1155':
                # Redirige a la página especial
                return redirect('catalogo_admin')  # Reemplaza 'catalogo_admin' con el nombre real de la URL de la página especial
            else:
                # Redirige a la página predeterminada
                return redirect('page')  # Reemplaza 'page' con el nombre real de la URL de la página predeterminada
        else:
            # Si la autenticación falla, muestra la página de inicio de sesión con un mensaje de error
            return render(request, 'login.html', {'error': 'Credenciales inválidas'})
    else:
        # Si el método de solicitud no es POST, muestra la página de inicio de sesión
        return render(request, 'login.html')



@login_required
def index(request):
    return render(request, 'index.html', {'user': request.user})


def reg(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # Success message or redirection logic here
            return redirect('login')  # Assuming you have a login view
    else:
        form = RegistrationForm()

    context = {'form': form}
    return render(request, 'register.html', context)
