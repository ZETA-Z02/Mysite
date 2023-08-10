from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import *

#Primer hola mundo con django, estara comentado para seguir con el libro
#muestran y envian solo mensajes, sin html sin mas
def hello(request):
    return HttpResponse("Hello World")

#muestra un dato discriminando por ID   
def mostrarId(request,id):
    responderId = TipoNoticia.objects.get(id=id)
    return HttpResponse("el tipo de noticia es: %s" % responderId.tipo)
#muestra solo el json sin mas, sin html, pero envia los datos, la CONSULTA FUNCIONA
def tipoNoticia(request):
    responder = list(TipoNoticia.objects.values())
    return JsonResponse(responder, safe=False)

#definir funciones para mostrar por pantalla, aqui se hace las consultas para mandar a mostrar en el html
def index(request):
    title = 'DJANGO!!!! utilizando variables'
    return render(request, "index.html",
    {
        'title': title,
    })

def noticiaTipoHtml(request):
    tipoDeNoticias = TipoNoticia.objects.all()
    return render(request, "tipodenoticia.html",
    {
       'tipoDeNoticias': tipoDeNoticias,
    })

def autores(request):
    autores = Autor.objects.all()
    paises = Paises.objects.all()
    return render(request, "autores.html",
    {
        'autores': autores,
        'paises':paises,
    })

def paises(request):
    paises = Paises.objects.all()
    return render(request, "paises.html","autor.html",
    {
        'paises' : paises,
    })

def contactos(request):
    return render(request, "contactos.html")

def datosAutores(request):
    autores = Autor.objects.all()
    paises = Paises.objects.all()
    documentos = TipoDoc.objects.all()
    for autor in autores:
        if autor.estado==1:
            autor.estadoActual='Activo'
        else:
            autor.estadoActual='Inactivo'
    for pais in paises:
        for autor in autores:
            if pais.codigo==autor.pais_id:
                autor.paisActual=pais.Nombre
    for documento in documentos:
        for autor in autores:
            if documento.id == autor.tipodoc_id:
                autor.documentoActual = documento.descripcion                
    return render(request, "datosAutores.html",
    {
        'autores':autores,
        'paises':paises,
        'documentos':documentos,
    }
    )

def noticias(request):
    tipoNoticias = TipoNoticia.objects.all()
    noticias = Noticia.objects.all()
    return render(request, "noticias.html",
    {
       'tipoNoticias': tipoNoticias,
       'noticias': noticias,
    })
    
