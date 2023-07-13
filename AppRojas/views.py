from django.shortcuts import render
from django.http import HttpResponse
from django.db import models
from AppRojas.models import Peliculas,Series,Musica
from AppRojas.forms import MusicaFormulario

def inicio(request):
    return render(request,"AppRojas/inicio.html")


def peliculas(request):

    return render(request, "AppRojas/peliculas.html")

def series(request):
    return render(request, "AppRojas/series.html")

def musica(request):
    
    
    if request.method == 'POST':

      miFormulario= MusicaFormulario(request.POST)
      print(miFormulario)

      if miFormulario.is_valid:

         informacion= miFormulario.cleaned_data
         musica= Musica(artista=informacion['artista'],genero=informacion['genero'],disco=informacion['disco'])
         musica.save()
         return render(request,"AppRojas/inicio.html")
    else:
        
        miFormulario= MusicaFormulario()


    
    return render(request, "AppRojas/musica.html",{'miFormulario':miFormulario})
   
      
  




def busquedaMusica(request):
   return render(request, 'AppRojas/busquedaMusica.html')


def buscar(request):
   if request.GET["disco"]:

      disco= request.GET['disco']
      artista= Musica.objects.filter(disco__icontains=disco)
      genero= Musica.objects.filter(disco__icontains=disco)

      return render(request, 'AppRojas/inicio.html',{"artista":artista,"genero":genero,"disco":disco   })
   
   else:
      
      respuesta= "no existen datos ingresados"

   return render(request,'AppRojas/inicio.html',{'respuesta':respuesta})
      
    