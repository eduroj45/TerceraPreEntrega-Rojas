from django.http import HttpResponse



def peliculas(request):
    return HttpResponse('aqui se alojaran las peliculas')

def series(request):
    return HttpResponse('aqui se alojaran las series')

def musica(request):
    return HttpResponse('aqui se alojara la musica ')
