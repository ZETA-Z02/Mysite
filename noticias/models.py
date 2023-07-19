from django.core.validators import RegexValidator
from django.db import models
from django.utils import timezone

##ESTA CARPETA ESTA PARA CREAR LOS MODELOS
# Create your models here.

class TipoNoticia(models.Model):
    tipo = models.CharField("Tipo de Noticias", max_length=30, blank=False, null=False)
    descripcion = models.TextField("Descripcion del tipo de noticias", max_length=300, blank=False, null=False)

class Paises(models.Model):
    codigo = models.CharField(max_length=2, blank=False, null=False, primary_key=True)
    Nombre = models.CharField("Nombre del pais", max_length=50, blank=False, null=False)

class TipoDoc(models.Model):
    codigo = models.TextField("Descripcion del tipo de documento", max_length=20, blank=False, null=False)
    
class Autor(models.Model):
    tipodoc = models.ForeignKey(TipoDoc, on_delete=models.CASCADE, default=None)
    documento = models.CharField("Documento de indentidad", max_length=16, blank=False, null=False, primary_key=True)
    nombres = models.CharField("Nombre del autor", max_length=200, blank=False, null=False, default=None)
    apellidos = models.CharField("Apellidos", max_length=200, blank=False, null=False, default=None)
    image = models.ImageField(upload_to="images / ", blank=False, default=None)
    pais = models.ForeignKey(Paises, on_delete=models.CASCADE, default=None)
    estado = models.BooleanField("Activo", default=True, blank=False, null=False)
    correo = models.EmailField("Correo Electronico", max_length=254, blank=False, null=False, default=None, validators=[RegexValidator(regex=r"\S{1}@\S{2}\.\S{2}", message="Correo invalido")],)
    telefono = models.CharField("Telefono", max_length=20, blank=False, null=False,default=None) 
    fecha_creacion = models.DateField("Fecha de creacion", default=timezone.now, blank=False, null=False)

class Noticia(models.Model):
    titulo = models.CharField("Titulo de la noticia", max_length=200, blank=False, null=False)
    descripcion = models.TextField("Descripcion de la noticia", max_length=500, blank=False, null=False)
    fecha = models.DateTimeField("Fecha de creacion", default=timezone.now, blank=False, null=False)
    autor = models.ForeignKey(Autor, to_field="documento", on_delete=models.CASCADE, default=None)
    tipo = models.ForeignKey(TipoNoticia, on_delete=models.CASCADE, default=None )

class Contacto(models.Model):
    id = models.AutoField(primary_key=True)
    nombreu = models.CharField("Nombres", max_length=200, blank=False, null=False)
    correo = models.CharField("Correo Electronico", max_length=200, blank=False, null=False, default=None, validators=[RegexValidator(regex=r"\S{1}@\S{2}\.\S{2}", message="Correo invalido")],)
    mensaje = models.TextField("Mensaje", max_length=400, blank=False, null=False)
    fecha_creacion = models.DateField("Fecha de Creacion", auto_now=True, blank=False, null=False)
    teléfono = models.CharField("Telefono", max_length=20, blank = False, null = False, default = None)
    fecha_creación = models.DateField("Fecha de creacion", default=timezone.now, blank=False, null=False)
    
class Noticia(models.Model):
    titulo = models.CharField("Titulo de la notica", max_length=200, blank=False, null=False)
    descripcion = models.TextField("Descripcion de la noticia", max_length=500, blank=False, null=False)
    fecha = models.DateTimeField("fecha de creacion", default=timezone.now, blank=False, null=False)
    autor = models.ForeignKey(Autor, to_field="documento", on_delete=models.CASCADE, default=None)
    tipo = models.ForeignKey(TipoNoticia, on_delete=models.CASCADE, default=None)

class Contacto(models.Model):
    id = models.AutoField(primary_key=True)
    nombreu = models.CharField("Nombres", max_length=200, blank=False, null=False)
    correo = models.CharField("Correo Electronico", max_length=200, blank=False, null=False, default=None, validators=[RegexValidator(regex=r"\S{1}@\S{2}\.\S{2}",message="Correo invalido")])   
    mensaje = models.TextField("Mensaje", max_length=400, blank=False, null=False)
    fecha_creación = models.DateTimeField("Fecha de creacion", auto_now=True, blank=False, name=False)
