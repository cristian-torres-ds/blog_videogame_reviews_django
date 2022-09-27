from django import forms



class PosteoForm(forms.Form):
    titulo = forms.CharField(max_length=100)
    subtitulo = forms.CharField(max_length=100)
    cuerpo = forms.CharField(max_length=1000)