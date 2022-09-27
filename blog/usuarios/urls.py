from django.urls import path
from usuarios.views import *
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', inicio, name='inicio'),
    path('login/', login_request, name='login'),
    path('register/', register, name='register'),
    path('logout/', LogoutView.as_view(template_name='app_super/logout.html'), name='logout'),
    path('editar_perfil', editar_perfil, name='editar_perfil'),
    path('add_avatar/', add_avatar, name='add_avatar'),
]