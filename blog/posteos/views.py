from django.shortcuts import render
from posteos.forms import PosteoForm
from posteos.models import Posteo
from usuarios.views import obtener_avatar, obtener_receptores, obtener_usuarios, obtener_posteos
from django.contrib.auth.decorators import login_required
import datetime


@login_required
def nuevo_posteo(request):
    if request.method == 'POST':
        mi_formulario = PosteoForm(request.POST, request.FILES)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            posteo = Posteo(titulo = informacion['titulo'],
                            puntaje = informacion['puntaje'],
                            subtitulo = informacion['subtitulo'],
                            actualizado = datetime.datetime.now(),
                            user = request.user,
                            contenido = informacion['contenido'],
                            creado = datetime.datetime.now(),
                            imagen = informacion['imagen'],)

            posteo.save()
            return render(request, "posteos/posteo_detallado.html", {'posteo':posteo,
                                                                     'mensaje':'Review subida exitosamente!!!',
                                                                     'avatar':obtener_avatar(request),
                                                                     'usuarios':obtener_usuarios(),
                                                                     'receptores':obtener_receptores(request)})

    else:
        mi_formulario = PosteoForm()
    return render(request, "posteos/nuevo_posteo.html", {'autor':request.user,
                                                         'mi_formulario':mi_formulario,
                                                         'avatar':obtener_avatar(request)})


def busqueda_posteo(request):

    return render(request, "posteos/busqueda_posteo.html", {'avatar':obtener_avatar(request),
                                                            'usuarios':obtener_usuarios(),
                                                            'receptores':obtener_receptores(request)})


def buscar_posteo(request):
    if request.GET["titulo"]:
        titulo = request.GET["titulo"]
        titulos = Posteo.objects.filter(titulo__icontains=titulo)
        return render(request, "posteos/buscar_posteo.html", {'titulos':titulos,
                                                              'avatar':obtener_avatar(request),
                                                              'usuarios':obtener_usuarios(),
                                                              'receptores':obtener_receptores(request)})
    else:
        return render(request, "posteos/busqueda_posteo.html", {'mensaje':'Ingrese un título.',
                                                                'avatar':obtener_avatar(request),
                                                                'usuarios':obtener_usuarios(),
                                                                'receptores':obtener_receptores(request)})


def ver_posteos(request):
    lista_posteos = Posteo.objects.all().order_by('-creado')

    return render(request, "posteos/ver_posteos.html", {'lista_posteos':lista_posteos,
                                                        'avatar':obtener_avatar(request),
                                                        'usuarios':obtener_usuarios(),
                                                        'receptores':obtener_receptores(request)})


def posteo_detallado(request, id):
    posteo = Posteo.objects.get(id=id)

    return render(request, "posteos/posteo_detallado.html", {'posteo':posteo,
                                                             'avatar':obtener_avatar(request),
                                                             'usuarios':obtener_usuarios(),
                                                             'receptores':obtener_receptores(request)})


@login_required
def eliminar_posteo(request, id):
    posteo = Posteo.objects.get(id=id)
    posteo.delete()

    return render(request, "usuarios/inicio.html", {'mensaje':f'Review eliminado',
                                                    'avatar':obtener_avatar(request),
                                                    'usuarios':obtener_usuarios(),
                                                    'receptores':obtener_receptores(request),
                                                    'lista_posteos':obtener_posteos()})



@login_required
def editar_posteo(request, id):
    posteo = Posteo.objects.get(id=id)

    if request.method == 'POST':
        mi_formulario = PosteoForm(request.POST, request.FILES)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            posteo.titulo = informacion['titulo']
            posteo.puntaje = informacion['puntaje']
            posteo.subtitulo = informacion['subtitulo']
            posteo.contenido = informacion['contenido']
            posteo.actualizado = datetime.datetime.now()
            posteo.imagen = informacion['imagen']
            
            posteo.save()

            return render(request, "posteos/posteo_detallado.html", {'posteo':posteo,
                                                                     'mensaje':'Review editado exitosamente!!!',
                                                                     'avatar':obtener_avatar(request),
                                                                     'usuarios':obtener_usuarios(),
                                                                     'receptores':obtener_receptores(request)})
    
    else:
        mi_formulario = PosteoForm(initial={'titulo':posteo.titulo,
                                            'puntaje':posteo.puntaje,
                                            'subtitulo':posteo.subtitulo,
                                            'contenido':posteo.contenido})

    return render(request, "posteos/editar_posteo.html", {'mi_formulario':mi_formulario,
                                                          'posteo':posteo,
                                                          'avatar':obtener_avatar(request)})


def review_criteria(request):

    return render(request, "posteos/review_criteria.html", {'avatar':obtener_avatar(request),
                                                            'usuarios':obtener_usuarios(),
                                                            'receptores':obtener_receptores(request)})