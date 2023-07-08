from django.db import models


class Peliculas(models.Model):
    nombre= models.CharField(max_length=50)
    genero= models.CharField(max_length=30)
    año=models.IntegerField()

class Series(models.Model):
    nombre= models.CharField(max_length=50)
    genero= models.CharField(max_length=30)
    año=models.IntegerField()

class Musica(models.Model):
    artista= models.CharField(max_length=50)
    genero= models.CharField(max_length=30)
    disco=models.CharField(max_length=50)
    



