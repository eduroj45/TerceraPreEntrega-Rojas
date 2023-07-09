from django.shortcuts import render
from django.http import HttpResponse

def inicio(request):
    return render(request,"AppRojas/inicio.html")


def peliculas(request):

    return render(request, "AppRojas/peliculas.html")

def series(request):
    return render(request, "AppRojas/series.html")

def musica(request):
    return render(request, "AppRojas/musica.html")