from django.urls import path, include
from django.conf.urls.static import static
from mysite import settings
from . import views

urlpatterns = [
    path('',views.index,name = 'index'),
    path('hola',views.hello,name = 'hola'),
    path('tipoNoticia',views.tipoNoticia,name = 'tipoNoticia'),
    path('ver/<int:id>',views.mostrarId, name = 'verId'),
    path('tiponoticia/',views.noticiaTipoHtml, name = 'noticiaTipoHtml'),
    path('autores/',views.autores, name= 'autores'),
    path('contactos/',views.contactos, name= 'contactos'),
    path('formulario-contactos/', views.formContactos, name='form_contactos'),
    path('datosAutores/',views.datosAutores, name= 'datosAutores'),
    path('noticias/',views.noticias, name= 'noticias'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
