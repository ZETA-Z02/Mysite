from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import TipoNoticia, Autor, Paises

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

def noticia(request):
    responder = TipoNoticia.objects.all()
    return render(request, "tipodenoticia.html",
    {
       'responder': responder,
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
    return render(request, "paises.html",
    {
        'paises' : paises,
    })
    
def contactos(request):
    return render(request, "contactos.html")

def datosAutores(request):
    return render(request, "datosAutores.html")

def noticias(request):
    return render(request, "noticias.html")