
"""VitalCare URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from core import views

urlpatterns = [
    path('', views.index, name='index'),
    path('pacientes', views.lista_pacientes, name='lista_pacientes'),
    path('presentacion/', views.presentacion, name='presentacion'),
    path('mision/', views.mision, name='mision'),
    path('vision/', views.vision, name='vision'),
    path('contacto/', views.contacto, name='contacto'),
    path('admin/', admin.site.urls),
    path('home/', views.base_home, name='base_home'),
    path('bodega/', views.inventario, name='bodega'),
    path('login/', views.login, name='login'),
    path('agenda/', views.agenda, name='agenda'),
    path('admin/', admin.site.urls),
]
