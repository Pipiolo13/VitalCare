from django.shortcuts import render, HttpResponse

# Create your views here.
def loguin(request):
    return HttpResponse("<h1>Pgina de logueo</h1>")