from django.urls import path
from mensajes.views import *


urlpatterns = [
    path('nuevo_mensaje/', nuevo_mensaje, name='nuevo_mensaje'),
    path('nuevo_mensaje/', nuevo_mensaje, name='nuevo_mensaje'),
    path('ver_mensajes/<id>', ver_mensajes, name='ver_mensajes'),
]