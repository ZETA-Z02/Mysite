# Register your models here.

from django.contrib import admin
from .models import TipoNoticia,Paises,TipoDoc,Autor,Noticia,Contacto

class TipoNoticiaAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'descripcion')
    list_filter = ('tipo','descripcion')

class PaisesAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'Nombre')
    list_filter = ('codigo','Nombre')

class TipoDocAdmin(admin.ModelAdmin):
    list_display = ('id', 'descripcion')
    list_filter = ('id', 'descripcion')

class AutorAdmin(admin.ModelAdmin):
    list_display = ('tipodoc','documento','nombres','apellidos','image')
    list_filter = ('documento', 'nombres', 'apellidos')

class NoticiaAdmin(admin.ModelAdmin):
    list_display = ('titulo','descripcion', 'fecha')
    list_filter = ('titulo', 'descripcion')
    
class ContactoAdmin(admin.ModelAdmin):
    list_display = ('id','nombreu','correo','mensaje')
    list_filter = ('nombreu', 'correo')
    

admin.site.register(TipoNoticia, TipoNoticiaAdmin)
admin.site.register(Paises, PaisesAdmin)
admin.site.register(TipoDoc, TipoDocAdmin)
admin.site.register(Autor, AutorAdmin) 
admin.site.register(Noticia, NoticiaAdmin)
admin.site.register(Contacto, ContactoAdmin)