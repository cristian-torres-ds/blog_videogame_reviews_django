from django.shortcuts import render
from posteos.forms import PosteoForm
from posteos.models import Posteo
from usuarios.views import obtener_avatar
from django.contrib.auth.decorators import login_required
import datetime


@login_required
def nuevo_posteo(request):
    if request.method == 'POST':
        mi_formulario = PosteoForm(request.POST)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            posteo = Posteo(titulo = informacion['titulo'],
                            puntaje = informacion['puntaje'],
                            subtitulo = informacion['subtitulo'],
                            actualizado = datetime.datetime.now(),
                            user = request.user,
                            contenido = informacion['contenido'],
                            creado = datetime.datetime.now())

            posteo.save()
            return render(request, "usuarios/inicio.html", {'autor':request.user, "mensaje":"Review subida exitosamente.", 'avatar':obtener_avatar(request)})
    else:
        mi_formulario = PosteoForm()
    return render(request, "posteos/nuevo_posteo.html", {'autor':request.user, "mi_formulario":mi_formulario, 'avatar':obtener_avatar(request)})


@login_required
def busqueda_posteo(request):

    return render(request, "posteos/busqueda_posteo.html", {'avatar':obtener_avatar(request)})


@login_required
def buscar_posteo(request):
    if request.GET["titulo"]:
        titulo = request.GET["titulo"]
        titulos = Posteo.objects.filter(titulo__icontains=titulo)
        return render(request, "posteos/buscar_posteo.html", {"titulos":titulos, 'avatar':obtener_avatar(request)})
    else:
        return render(request, "posteos/busqueda_posteo.html", {"mensaje":"Ingrese un título.", 'avatar':obtener_avatar(request)})


@login_required
def ver_posteos(request):
    lista_posteos = Posteo.objects.all().order_by('creado')

    return render(request, "posteos/ver_posteos.html", {"lista_posteos":lista_posteos, 'avatar':obtener_avatar(request)})


def posteo_detallado(request, id):
    posteo = Posteo.objects.get(id=id)

    return render(request, "posteos/posteo_detallado.html", {"posteo":posteo, 'avatar':obtener_avatar(request)})


@login_required
def eliminar_posteo(request, id):
    posteo = Posteo.objects.get(id=id)
    posteo.delete()

    return render(request, "usuarios/inicio.html", {'mensaje':f"Review eliminado", 'avatar':obtener_avatar(request)})



@login_required
def editar_posteo(request, id):
    posteo = Posteo.objects.get(id=id)

    if request.method == 'POST':
        mi_formulario = PosteoForm(request.POST)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            posteo.titulo = informacion['titulo']
            posteo.puntaje = informacion['puntaje']
            posteo.subtitulo = informacion['subtitulo']
            posteo.contenido = informacion['contenido']
            posteo.actualizado = datetime.datetime.now()
            
            posteo.save()

            return posteo_detallado(request, id=id)
    
    else:
        mi_formulario = PosteoForm(initial={'titulo':posteo.titulo,
                                            'puntaje':posteo.puntaje,
                                            'subtitulo':posteo.subtitulo,
                                            'contenido':posteo.contenido})

    return render(request, "posteos/editar_posteo.html", {'mi_formulario':mi_formulario, 'posteo':posteo, 'avatar':obtener_avatar(request)})