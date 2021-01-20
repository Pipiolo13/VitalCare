from django.shortcuts import render, HttpResponse

# Create your views here.....


html_cabecera =  """
    <h1>WELCOME</h1>
    <ul>
        <li><a href="/">Home</a></li>
        <li><a href="/Doctores">DOCTORES</a></li>
        

    </ul>
""" 
def  home ( inicio ):
    return  HttpResponse ( "<h1> SISTEMA VITALCARE </h1>" )


def  Doctores ( doctores ):
    return  HttpResponse ( "<h1> HISTORIAL CLINICO DE PACIENTES </h1>" )