from django.shortcuts import render, HttpResponse

# Create your views here.


def enfermeria(request):
    return render(request, "core/enfermeria.html")    
