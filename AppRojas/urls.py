from django.urls import path
from AppRojas import views


urlpatterns = [
    path('',views.inicio,name="Inicio"),
    path('peliculas',views.peliculas,name="Peliculas"),
    path('series', views.series,name="Series"),
    path('musica',views.musica,name="Musica"),
    path('musicaAgregada', views.musica, name='musicaAgregada')    
    path('busquedaMusica', views.busquedaMusica, name="BusquedaMusica"),
    path('buscar/', views.buscar),
]
