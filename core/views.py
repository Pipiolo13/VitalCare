from django.shortcuts import render, HttpResponse

# Create your views here.....


def doctor (request):
    return  render(request,"core/BaseDoctor.html")