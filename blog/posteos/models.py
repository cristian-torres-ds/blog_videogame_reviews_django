from django.db import models
from django.contrib.auth.models import User


class Posteo(models.Model):
    titulo = models.CharField(max_length=200, unique=True)
    subtitulo = models.CharField(max_length=200, unique=True)
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    puntaje = models.IntegerField()
    actualizado = models.DateTimeField()
    contenido = models.TextField()
    creado = models.DateTimeField()


    class Meta:
        ordering = ['creado']

    def __str__(self):
        return self.titulo