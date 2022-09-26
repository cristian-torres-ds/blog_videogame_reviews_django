from django.db import models

class Mensaje(models.Model):
    emisor = models.CharField(max_length=50)
    receptor = models.CharField(max_length=50)
    mensaje = models.CharField(max_length=500)

    def __str__(self):
        return f"De: {self.emisor}, para: {self.receptor}"