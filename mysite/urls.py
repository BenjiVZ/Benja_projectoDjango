"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from myapp.views import page_1,menu1,menu2
from app_users.views import reg,user_login
from app_admin.views import catalogo_admin
from app_carrito.views import carrito
from app_catalogo.views import catalogo

# urls.py

from django.conf import settings
from django.conf.urls.static import static
""" from django.contrib.auth.views import LoginView """

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', page_1, name='page'),
    path('login/', user_login, name='login'),
    path('register/', reg, name='register'),
    path('catalogo/', catalogo, name='catalogo'),
    path('cart/', carrito, name='carrito'),
    path('admin_add/', catalogo_admin, name='catalogo_admin'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

"""   path('login/', LoginView.as_view(template_name='login.html'), name='login'), """