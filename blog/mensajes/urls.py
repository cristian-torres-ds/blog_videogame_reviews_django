from django.urls import path
from mensajes.views import *


urlpatterns = [
    path('nuevo_mensaje/', nuevo_mensaje, name='nuevo_mensaje'),
    path('ver_mensajes/', ver_mensajes, name='ver_mensajes'),
]