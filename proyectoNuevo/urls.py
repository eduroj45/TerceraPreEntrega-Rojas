
from django.contrib import admin
from django.urls import path
from proyectoNuevo.views import peliculas,series,musica

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Peliculas/',peliculas),
    path('Series/', series),
    path('Musica',musica),
]