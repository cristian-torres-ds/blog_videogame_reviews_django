from django.shortcuts import render
from usuarios.models import Avatar
from usuarios.forms import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from posteos.models import Posteo
from mensajes.models import Mensaje


def inicio(request):

    return render(request, "usuarios/inicio.html", {'lista_posteos':obtener_posteos(),
                                                    'avatar':obtener_avatar(request),
                                                    'usuarios':obtener_usuarios(),
                                                    'receptores':obtener_receptores(request)})


def acerca_de(request):

    return render(request, "usuarios/acerca_de.html", {'avatar':obtener_avatar(request),
                                                       'usuarios':obtener_usuarios(),
                                                       'receptores':obtener_receptores(request)})


def login_request(request):
    if request.method=="POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')

            user = authenticate(username=usuario, password=contra)

            if user is not None:
                login(request, user)

                return render(request, "usuarios/inicio.html", {'mensaje':f"Bienvenido {usuario}!!!",
                                                                'avatar':obtener_avatar(request),
                                                                'usuarios':obtener_usuarios(),
                                                                'lista_posteos':obtener_posteos(),
                                                                'receptores':obtener_receptores(request)})
            else:
                return render(request, "usuarios/login.html", {'formulario':form,
                                                               'mensaje':'Usuario o contraseña incorrectos',
                                                               'avatar':obtener_avatar(request),
                                                               'usuarios':obtener_usuarios()})
        else:
            return render(request, "usuarios/login.html", {'formulario':form,
                                                           'mensaje':'Usuario o contraseña incorrectos',
                                                           'avatar':obtener_avatar(request),
                                                           'usuarios':obtener_usuarios()})
    else:
        form=AuthenticationForm()
        return render(request, "usuarios/login.html", {'formulario':form,
                                                       'avatar':obtener_avatar(request),
                                                       'usuarios':obtener_usuarios()})


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()

            return render(request, "usuarios/inicio.html", {'mensaje':f'Usuario {username} creado correctamente.',
                                                            'avatar':obtener_avatar(request),
                                                            'usuarios':obtener_usuarios(),
                                                            'lista_posteos':obtener_posteos()})
    else:
        form = UserRegisterForm()
    
    return render(request, "usuarios/register.html", {'formulario':form,
                                                      'avatar':obtener_avatar(request),
                                                      'usuarios':obtener_usuarios()})


@login_required
def editar_perfil(request):
    usuario = request.user
    if request.method == 'POST':
        form = UserEditForm(request.POST)
        if form.is_valid():
            informacion = form.cleaned_data

            usuario.email = informacion['email']
            usuario.first_name = informacion['first_name']
            usuario.last_name = informacion['last_name']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            usuario.save()

            return render(request, "usuarios/inicio.html", {'avatar':obtener_avatar(request),
                                                            'usuarios':obtener_usuarios(),
                                                            'receptores':obtener_receptores(request),
                                                            'mensaje':'Prefil editado correctamente.',
                                                            'lista_posteos':obtener_posteos()})
    
    else:
        form = UserEditForm(initial={'email':usuario.email,
                                     'first_name':usuario.first_name,
                                     'last_name':usuario.last_name})

    return render(request, "usuarios/editar_perfil.html", {'mi_formulario':form,
                                                           'usuario':usuario,
                                                           'avatar':obtener_avatar(request),
                                                           'usuarios':obtener_usuarios(),
                                                           'receptores':obtener_receptores(request)})


@login_required
def add_avatar(request):
    if request.method == 'POST':
        formulario = AvatarForm(request.POST, request.FILES)
        if formulario.is_valid():
            avatar_viejo = Avatar.objects.filter(user=request.user)
            if(len(avatar_viejo)>0):
                avatar_viejo[0].delete()
            avatar = Avatar(user=request.user, imagen=formulario.cleaned_data['imagen'])
            avatar.save()

            return render(request, 'usuarios/inicio.html', {'usuario':request.user,
                                                            'mensaje':'Avatar guardado',
                                                            'imagen':avatar.imagen.url,
                                                            'avatar':obtener_avatar(request),
                                                            'usuarios':obtener_usuarios(),
                                                            'lista_posteos':obtener_posteos(),
                                                            'receptores':obtener_receptores(request)})
        else:
            return render(request, 'usuarios/add_avatar.html', {'usuario':request.user,
                                                                'mensaje':'Formulario inválido',
                                                                'avatar':obtener_avatar(request),
                                                                'usuarios':obtener_usuarios(),
                                                                'receptores':obtener_receptores(request)})
    else:
        formulario = AvatarForm()
        return render(request, "usuarios/add_avatar.html", {'mi_formulario':formulario,
                                                            'usuario':request.user,
                                                            'avatar':obtener_avatar(request),
                                                            'usuarios':obtener_usuarios(),
                                                            'receptores':obtener_receptores(request)})



def obtener_avatar(request):
    if request.user.is_authenticated:
        lista = Avatar.objects.filter(user=request.user)
        if len(lista)!=0:
            imagen = lista[0].imagen.url
        else:
            imagen = "/media/avatares/default.png"
    else:
        imagen = "/media/avatares/default.png"
    return imagen



def obtener_usuarios():
    lista_usuarios = User.objects.all().exclude(username="admin")

    return lista_usuarios



def usuario_detallado(request, id):
    usuario = User.objects.get(id=id)
    posteos = Posteo.objects.filter(user_id=id)
    foto_lista = Avatar.objects.filter(user_id=id)
    if len(foto_lista)!=0:
        foto = foto_lista[0].imagen.url
    else:
        foto = "/media/avatares/default.png"

    return render(request, "usuarios/usuario_detallado.html", {'usuario':usuario,
                                                               'avatar':obtener_avatar(request),
                                                               'usuarios':obtener_usuarios(),
                                                               'posteos':posteos,
                                                               'foto':foto,
                                                               'receptores':obtener_receptores(request)})


# Se colocó aquí porque si se la coloca en mensajes.views trae el siquiente error:
# ImportError: cannot import name 'obtener_avatar' from partially initialized module 'usuarios.views' (most likely due to a circular import)
def obtener_receptores(request):
    if request.user.is_authenticated:
        lista_receptores_unique = []

        lista_chats = Mensaje.objects.filter(emisor_id=request.user.id).values_list('receptor_id', flat=True)
        for receptor in lista_chats:
            if receptor not in lista_receptores_unique:
                lista_receptores_unique.append(receptor)

        lista_chats_2 = Mensaje.objects.filter(receptor_id=request.user.id).values_list('emisor_id', flat=True)
        for emisor in lista_chats_2:
            if emisor not in lista_receptores_unique:
                lista_receptores_unique.append(emisor)

        receptores = User.objects.filter(id__in=lista_receptores_unique)
    
    else:
        receptores = []

    return receptores



def acerca_de(request):
    foto = "/media/torres_team.jpg"

    return render(request, "usuarios/acerca_de.html", {'avatar':obtener_avatar(request),
                                                       'usuarios':obtener_usuarios(),
                                                       'foto':foto,
                                                       'receptores':obtener_receptores(request)})


def obtener_posteos():
    lista_posteos = Posteo.objects.all().order_by('-creado')
    if len(lista_posteos) > 3:
        lista_posteos = lista_posteos[0:3]
    return lista_posteos
