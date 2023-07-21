# Register your models here.

from django.contrib import admin
from .models import TipoNoticia,Paises,TipoDoc,Autor,Noticia,Contacto

admin.site.register(TipoNoticia)
admin.site.register(Paises)
admin.site.register(TipoDoc)
admin.site.register(Autor)
admin.site.register(Noticia)
admin.site.register(Contacto)

