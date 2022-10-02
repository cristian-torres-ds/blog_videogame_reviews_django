from django.shortcuts import render
#from django.http import HttpResponse
from django.shortcuts import render
#import datetime
from .models import *
from .forms import *
#from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required


def inicio(request):

    return render(request, "usuarios/inicio.html", {'avatar':obtener_avatar(request)})


def acerca_de(request):

    return render(request, "usuarios/acerca_de.html", {'avatar':obtener_avatar(request)})


def login_request(request):
    if request.method=="POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')

            user = authenticate(username=usuario, password=contra)

            if user is not None:
                login(request, user)
                return render(request, "usuarios/inicio.html", {'mensaje':f"Bienbenido {usuario}", 'avatar':obtener_avatar(request)})
            else:
                return render(request, "usuarios/login.html", {"formulario":form, "mensaje":"Usuario o contraseña incorrectos", 'avatar':obtener_avatar(request)})
        else:
            return render(request, "usuarios/login.html", {"formulario":form, "mensaje":"Usuario o contraseña incorrectos", 'avatar':obtener_avatar(request)})
    else:
        form=AuthenticationForm()
        return render(request, "usuarios/login.html", {'formulario':form, 'avatar':obtener_avatar(request)})


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request, "usuarios/inicio.html", {'mensaje':f"Usuario {username} creado correctamente.", 'avatar':obtener_avatar(request)})
    else:
        form = UserRegisterForm()
    
    return render(request, "usuarios/register.html", {'formulario':form, 'avatar':obtener_avatar(request)})


@login_required
def editar_perfil(request):
    usuario = request.user
    if request.method == 'POST':
        form = UserEditForm(request.POST)
        if form.is_valid():
            informacion = form.cleaned_data

            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            usuario.save()

            return render(request, "usuarios/inicio.html", {'avatar':obtener_avatar(request)})
    
    else:
        form = UserEditForm(initial={'email':usuario.email})

    return render(request, "usuarios/editar_perfil.html", {'mi_formulario':form, 'usuario':usuario, 'avatar':obtener_avatar(request)})


@login_required
def add_avatar(request):
    if request.method == 'POST':
        formulario = AvatarForm(request.POST, request.FILES)
        if formulario.is_valid():
            # Para eliminar avatar antiguo
            avatar_viejo = Avatar.objects.filter(user=request.user)
            if(len(avatar_viejo)>0):
                avatar_viejo[0].delete()
            # Añadir avatar nuevo
            avatar = Avatar(user=request.user, imagen=formulario.cleaned_data['imagen'])
            avatar.save()
            return render(request, 'usuarios/inicio.html', {'usuario':request.user, 'mensaje':'Avatar guardado', 'imagen':avatar.imagen.url, 'avatar':obtener_avatar(request)})
        else:
            return render(request, 'usuarios/add_avatar.html', {'usuario':request.user, 'mensaje':'Formulario inválido', 'avatar':obtener_avatar(request)})
    else:
        formulario = AvatarForm()
        return render(request, "usuarios/add_avatar.html", {'mi_formulario':formulario, 'usuario':request.user, 'avatar':obtener_avatar(request)})


def obtener_avatar(request):
    try:
        lista = Avatar.objects.filter(user=request.user)
    except TypeError:
        imagen = "/media/avatares/default.png"
    else:
        if len(lista)!=0:
            imagen = lista[0].imagen.url
        else:
            imagen = "/media/avatares/default.png"
    return imagen