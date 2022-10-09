from django.db import models
from django.contrib.auth.models import User

class Mensaje(models.Model):
    emisor = models.ForeignKey(User, null=True, related_name='emisor', on_delete=models.CASCADE)
    receptor = models.ForeignKey(User, null=True, related_name='receptor', on_delete=models.CASCADE)
    contenido = models.CharField(max_length=1000)
    creado = models.DateTimeField()

    class Meta:
        ordering = ['creado']

    def __str__(self):
        return f"De: {self.emisor}, para: {self.receptor}"