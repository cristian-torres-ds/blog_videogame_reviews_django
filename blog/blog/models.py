from django.db import models
from django.contrib.auth.models import User



class Avatar(models.Model):
    # Vínculo con el usuario
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # Subcarpeta avatares de media
    imagen = models.ImageField(upload_to='avatares')