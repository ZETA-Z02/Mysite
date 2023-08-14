from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse
from .models import *
from .forms import *
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
    #name = input("ingresa tu nombre")
    return render(request, "index.html",
    {
        'title': title,
        #'name': name,
    })

def noticiaTipoHtml(request):
    if request.method == 'POST':
        form = TipoNoticiaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('noticias:noticiaTipoHtml')
    else:
        form = TipoNoticiaForm()
        
    TipoDeNoticias = TipoNoticia.objects.all()
    return render(request, "tipodenoticia.html",
    {
       'tipoDeNoticias': TipoDeNoticias,
       'formTipo':form,
    })

def autores(request):
    if request.method == 'POST':
        form = AutorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('noticias:datosAutores')
    else:
        form = AutorForm()

    autores = Autor.objects.all()
    paises = Paises.objects.all()
    return render(request, "autores.html",
    {
        'autores': autores,
        'paises':paises,
        'autorForm':form,
    })

def paises(request):
    paises = Paises.objects.all()
    return render(request, "paises.html","autor.html",
    {
        'paises' : paises,
    })

def contactos(request):
    contactos = Contacto.objects.all()
    return render(request, "contactos.html",
    {
        'contactos':contactos,
    })

def formContactos(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('noticias:contactos')
    else:
        form = ContactoForm()
    
    return render(request, "contactos.html",
    {
        'form':form,   
    })
            

def datosAutores(request):
    autores = Autor.objects.all()
    var= TipoDoc.objects.get(id=2)
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
        'dato':var
    }
    )

def noticias(request):
    if request.method == 'POST':
        form = NoticiaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('noticias:noticias')
    else:
        form = NoticiaForm()
    tipoNoticias = TipoNoticia.objects.all()
    noticias = Noticia.objects.all()
    return render(request, "noticias.html",
    {
       'tipoNoticias': tipoNoticias,
       'noticias': noticias,
       'noticiaForm': form,
    })
    
