from django.shortcuts import render
from mensajes.forms import MensajeForm
from mensajes.models import Mensaje
import datetime
from usuarios.views import obtener_avatar, obtener_usuarios, obtener_receptores
from django.contrib.auth.decorators import login_required
from usuarios.models import Avatar
from django.contrib.auth.models import User


@login_required
def nuevo_mensaje(request):
    if request.method == 'POST':
        mi_formulario = MensajeForm(request.POST)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            mensaje = Mensaje(emisor = request.user,
                              receptor = informacion['receptor'],
                              contenido = informacion['contenido'],
                              creado = datetime.datetime.now())

            mensaje.save()

            return ver_mensajes(request, mensaje.receptor.id)

    else:
        mi_formulario = MensajeForm()
    return render(request, "mensajes/nuevo_mensaje.html", {'mi_formulario':mi_formulario,
                                                           'avatar':obtener_avatar(request),
                                                           'usuarios':obtener_usuarios(),
                                                           'receptores':obtener_receptores(request)})


@login_required
def ver_mensajes(request, id):
    receptor = User.objects.get(id=id)

    lista_mensajes = obtener_mensajes(request, id)

    foto_lista = Avatar.objects.filter(user_id=id)
    if len(foto_lista)!=0:
        foto = foto_lista[0].imagen.url
    else:
        foto = "/media/avatares/default.png"

    return render(request, "mensajes/ver_mensajes.html", {'avatar':obtener_avatar(request),
                                                          'usuarios':obtener_usuarios(),
                                                          'lista_mensajes':lista_mensajes,
                                                          'foto':foto,
                                                          'receptor':receptor,
                                                          'receptores':obtener_receptores(request)})


def obtener_mensajes(request, id):
    lista_mensajes_mios = Mensaje.objects.filter(emisor_id=request.user.id).filter(receptor_id=id).values_list('id', flat=True)
    lista_mensajes_otro = Mensaje.objects.filter(emisor_id=id).filter(receptor_id=request.user.id).values_list('id', flat=True)

    lista_mensajes_id = []

    for mensaje in lista_mensajes_mios:
            if mensaje not in lista_mensajes_id:
                lista_mensajes_id.append(mensaje)

    for mensaje in lista_mensajes_otro:
            if mensaje not in lista_mensajes_id:
                lista_mensajes_id.append(mensaje)

    lista_mensajes = Mensaje.objects.filter(id__in=lista_mensajes_id).order_by('creado')

    return lista_mensajes