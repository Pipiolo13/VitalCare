from django.shortcuts import render, HttpResponse

# Create your views here.

def enfermeria(request):
    return HttpResponse("<h1>Modulo de enfermeria</h1>")
