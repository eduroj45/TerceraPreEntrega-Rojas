from django.urls import path
from AppRojas import views


urlpatterns = [
    path('',views.inicio),
    path('peliculas',views.peliculas),
    path('series', views.series),
    path('musica',views.musica),
]