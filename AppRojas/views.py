from django.shortcuts import render
from django.http import HttpResponse
from django.db import models
from AppRojas.models import Peliculas,Series,Musica
from AppRojas.forms import MusicaFormulario,PeliculasFormulario,SeriesFormulario

def inicio(request):
    return render(request,"AppRojas/inicio.html")


def peliculas(request):
      
    
    if request.method == 'POST':

      miFormulario= PeliculasFormulario(request.POST)
      print(miFormulario)

      if miFormulario.is_valid:

         informacion= miFormulario.cleaned_data
         pelicula= Peliculas(nombre=informacion['nombre'],genero=informacion['genero'],año=informacion['año'])
         pelicula.save()
         return render(request,"AppRojas/inicio.html")
    else:
        
        miFormulario=PeliculasFormulario()


    
    return render(request, "AppRojas/peliculas.html",{'miFormulario':miFormulario})

   

def series(request):
       
    if request.method == 'POST':

      miFormulario= SeriesFormulario(request.POST)
      print(miFormulario)

      if miFormulario.is_valid:

         informacion= miFormulario.cleaned_data
         serie= Series(nombre=informacion['nombre'],genero=informacion['genero'],año=informacion['año'])
         serie.save()
         return render(request,"AppRojas/inicio.html")
    else:
        
        miFormulario=SeriesFormulario()


    
    return render(request, "AppRojas/series.html",{'miFormulario':miFormulario})


def musica(request):
    
    
    if request.method == 'POST':

      miFormulario= MusicaFormulario(request.POST)
      print(miFormulario)

      if miFormulario.is_valid:

         informacion= miFormulario.cleaned_data
         musica= Musica(artista=informacion['artista'],genero=informacion['genero'],disco=informacion['disco'])
         musica.save()
         return render(request,"AppRojas/musicaAgregada.html")
    else:
        
        miFormulario= MusicaFormulario()


    
    return render(request, "AppRojas/musica.html",{'miFormulario':miFormulario})
   
      
  




def busquedaMusica(request):
   return render(request, 'AppRojas/busquedaMusica.html')


def buscar(request):
   if request.GET["disco"]:

      disco= request.GET['disco']
      
      artista= Musica.objects.filter(disco__icontains=disco)

      

      return render(request, 'AppRojas/inicio.html',{"artista":artista,"disco":disco   })
   
   else:
      
      respuesta= "no existen datos ingresados"

   return render(request,'AppRojas/inicio.html',{'respuesta':respuesta})
      
    
