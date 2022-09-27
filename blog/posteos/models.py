from django.db import models

class Posteo(models.Model):
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=100)
    cuerpo = models.CharField(max_length=1000)
    fecha = models.DateField()

    def __str__(self):
        return f"Autor: {self.autor}, Titulo: {self.receptor}"