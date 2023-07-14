from django import forms


class PeliculasFormulario(forms.Form):
    nombre=forms.CharField()
    genero=forms.CharField()
    año= forms.IntegerField()

class SeriesFormulario(forms.Form):
    nombre=forms.CharField()
    genero=forms.CharField()
    año= forms.IntegerField()
    
class MusicaFormulario (forms.Form):
    artista=forms.CharField()
    genero=forms.CharField()
    disco=forms.CharField()

