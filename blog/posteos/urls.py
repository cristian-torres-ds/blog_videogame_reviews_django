from django.urls import path
from posteos.views import *


urlpatterns = [
    path('nuevo_posteo/', nuevo_posteo, name='nuevo_posteo'),
    path('ver_posteos/', ver_posteos, name='ver_posteos'),
    path('buscar_posteo/', buscar_posteo, name='buscar_posteo'),
    path('busqueda_posteo/', busqueda_posteo, name='busqueda_posteo'),
    path('editar_posteo/<id>', editar_posteo, name='editar_posteo'),
    path('eliminar_posteo/<id>', eliminar_posteo, name='eliminar_posteo'),
    path('posteo_detallado/<id>', posteo_detallado, name='posteo_detallado'),
    path('review_criteria/', review_criteria, name='review_criteria'),
]