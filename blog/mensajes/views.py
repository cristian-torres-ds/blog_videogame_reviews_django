from django.shortcuts import render
from mensajes.forms import MensajeForm, ResponderForm
from mensajes.models import Mensaje
import datetime
from usuarios.views import obtener_avatar
from usuarios.views import obtener_usuarios
from django.contrib.auth.decorators import login_required
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
            lista_mensajes = Mensaje.objects.filter(emisor_id=request.user.id).filter(receptor_id=mensaje.receptor.id).order_by('-creado')
            return render(request, "mensajes/ver_mensajes_nuevo.html", {'lista_mensajes':lista_mensajes,
                                                                        'avatar':obtener_avatar(request),
                                                                        'usuarios':obtener_usuarios()})
    else:
        mi_formulario = MensajeForm()
    return render(request, "mensajes/nuevo_mensaje.html", {'mi_formulario':mi_formulario,
                                                           'avatar':obtener_avatar(request),
                                                           'usuarios':obtener_usuarios()})


@login_required
def ver_mensajes(request, id):
    lista_mensajes = Mensaje.objects.filter(emisor_id=request.user.id).filter(receptor_id=id).order_by('creado')

    return render(request, "mensajes/ver_mensajes.html", {'avatar':obtener_avatar(request),
                                                          'usuarios':obtener_usuarios(),
                                                          'lista_mensajes':lista_mensajes,})