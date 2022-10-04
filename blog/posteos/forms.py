from django import forms
from posteos.models import Posteo
from ckeditor_uploader.fields import RichTextUploadingFormField



class PosteoForm(forms.Form):
    titulo = forms.CharField(max_length=200)
    puntaje = forms.IntegerField()
    subtitulo = forms.CharField(max_length=200)
    imagen = forms.ImageField(label="imagen")
    contenido = RichTextUploadingFormField()