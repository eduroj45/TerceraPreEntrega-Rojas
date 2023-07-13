from django import forms



class MusicaFormulario (forms.Form):
    artista=forms.CharField()
    genero=forms.CharField()
    disco=forms.CharField()

