
from django.shortcuts import render, HttpResponse


# Create your views here.

def base_home(request):
    return render(request, "core/base_home.html")


def inventario(request):
    return render(request, "core/bodega.html")


def home(request):
    return render(request, "core/home.html")


def listaPacientes(request):
    return render(request, "core/ListaPacientes.html")


def login(request):
    return render(request, "core/login.html")


def index(request):
    return render(request, "core/index.html")


def presentacion(request):
    return render(request, "core/presentacion.html")


def mision(request):
    return render(request, "core/mision.html")


def vision(request):
    return render(request, "core/vision.html")


def contacto(request):
    return render(request, "core/contacto.html")


def enfermeria(request):
    return render(request, "core/enfermeria.html")


def enfermeria(request):
    return render(request, "core/enfermeria.html")
