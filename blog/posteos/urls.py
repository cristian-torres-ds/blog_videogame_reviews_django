from django.urls import path
from posteos.views import *


urlpatterns = [
    path('nuevo_posteo/', nuevo_posteo, name='nuevo_mensaje'),
    path('ver_posteos/', ver_posteos, name='ver_mensajes'),
    path('buscar_posteo/', buscar_posteo, name='ver_mensajes'),
    path('busqueda_posteo/', busqueda_posteo, name='ver_mensajes'),
    path('editar_posteo/', editar_posteo, name='ver_mensajes'),
    path('eliminar_posteo/', eliminar_posteo, name='ver_mensajes'),
]