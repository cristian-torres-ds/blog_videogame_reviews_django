from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField


class Posteo(models.Model):
    titulo = models.CharField(max_length=200) # , unique=True
    subtitulo = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    puntaje = models.IntegerField()
    actualizado = models.DateTimeField()
    contenido = RichTextUploadingField()
    creado = models.DateTimeField()
    imagen = models.ImageField(upload_to='imagenes')

    class Meta:
        ordering = ['-creado']

    def __str__(self):
        return self.titulo