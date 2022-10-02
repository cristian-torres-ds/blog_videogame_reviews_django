from django import forms
from django.contrib.auth.models import User



class PosteoForm(forms.Form):
    titulo = forms.CharField(max_length=200)
    puntaje = forms.IntegerField()
    subtitulo = forms.CharField(max_length=200)
    contenido = forms.CharField(max_length=1000)
