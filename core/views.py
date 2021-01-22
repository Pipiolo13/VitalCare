from django.shortcuts import render, HttpResponse

# Create your views here.
def loguin(request):
    return render(request,"core/loguin.html")

