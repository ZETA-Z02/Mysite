from django.core.validators import RegexValidator
from django.db import models
from django.utils import timezone
from django.utils.safestring import mark_safe


##ESTA CARPETA ESTA PARA CREAR LOS MODELOS
# Create your models here.

class TipoNoticia(models.Model):
    tipo = models.CharField("Tipo de Noticias", max_length=30, blank=False, null=False)
    descripcion = models.TextField("Descripcion del tipo de noticias", max_length=300, blank=False, null=False)
    
    class Meta:
        verbose_name = "Tipo de Noticias"
        verbose_name_plural = "Tipos de Noticias"
        ordering = ["tipo"]
    
    def __str__(self):
        return '%s %s' % (self.tipo, self.descripcion)
        
class Paises(models.Model): 
    codigo = models.CharField(max_length=2, blank=False, null=False, primary_key=True)
    Nombre = models.CharField("Nombre del pais", max_length=50, blank=False, null=False)
    
    class Meta:
        verbose_name = "Paises"
        verbose_name = "Paises"
        ordering = ["Nombre"]
    def __str__(self):
        return '%s %s' % (self.codigo, self.Nombre)

class TipoDoc(models.Model):
    descripcion = models.TextField("Descripcion del tipo de documento", max_length=20, blank=False, null=False)
    
    class Meta:
        verbose_name = "Pais"
        verbose_name_plural = "Paises"
        ordering = ["descripcion"]  
    def __str__(self):
        return '%s' % (self.descripcion)

class Autor(models.Model):
    tipodoc = models.ForeignKey(TipoDoc, on_delete=models.CASCADE, default=None)
    documento = models.CharField("Documento de identidad", max_length=16, blank=False, null=False, primary_key=True)
    nombres = models.CharField("Nombre del autor", max_length=200, blank=False, null=False, default=None)
    apellidos = models.CharField("Apellidos", max_length=200, blank=False, null=False, default=None)
    def get_foto(self):
        if self.image:
            return mark_safe(u'<img src="%s" width="60" height="75"/>' % self.image.url)
        else:
            return ''
    get_foto.short_description = 'Photo'
    get_foto.admin_order_field = 'name'
    
    image = models.ImageField(upload_to='images/', blank=False, default=None)
    pais = models.ForeignKey(Paises, on_delete=models.CASCADE, default=None)
    estado = models.BooleanField("Activo", default=True, blank=False, null=False)
    correo = models.EmailField("Correo Electronico", max_length=254, blank=False, null=False, default=None, validators=[RegexValidator(regex=r"\S{1,}@\S{2,}\.\S{2,}", message="Correo invalido")])
    telefono = models.CharField("Telefono", max_length=20, blank=False, null=False, default=None)
    fecha_creacion = models.DateField("Fecha de creacion", default=timezone.now, blank=False, null=False)
    
    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autores"
        ordering = ['nombres', 'apellidos']

    def __str__(self):
        return '%s %s %s %s %s' % (self.tipodoc, self.documento, self.nombres, self.apellidos,self.image)

class Noticia(models.Model):
    titulo = models.CharField("Titulo de la noticia", max_length=200, blank=False, null=False)
    descripcion = models.TextField("Descripcion de la noticia", max_length=500, blank=False, null=False)
    fecha = models.DateTimeField("Fecha de creacion", default=timezone.now, blank=False, null=False)
    autor = models.ForeignKey(Autor, to_field="documento", on_delete=models.CASCADE, default=None)
    tipo = models.ForeignKey(TipoNoticia, on_delete=models.CASCADE, default=None )
    class Meta:
        verbose_name = "Noticia"
        verbose_name_plural = "Noticias"
        ordering = ['descripcion']
    def __str__(self):
        return '%s %s %s' % (self.titulo, self.descripcion, self.fecha)
 
class Contacto(models.Model):
    id = models.AutoField(primary_key=True)
    nombreu = models.CharField("Nombres", max_length=200, blank=False, null=False)
    correo = models.CharField("Correo Electronico", max_length=200, blank=False, null=False, default=None, validators=[RegexValidator(regex=r"\S{1}@\S{2}\.\S{2}", message="Correo invalido")],)
    mensaje = models.TextField("Mensaje", max_length=400, blank=False, null=False)
    fecha_creacion = models.DateField("Fecha de Creacion", auto_now=True, blank=False, null=False)
    teléfono = models.CharField("Telefono", max_length=20, blank = False, null = False, default = None)
    fecha_creación = models.DateField("Fecha de creacion", default=timezone.now, blank=False, null=False)
    
    class Meta:
        verbose_name = "Contacto"
        verbose_name_plural = "Contactos"
        ordering = ['id']
    def __str__(self):
        return '%s %s %s %s' % (self.id, self.nombre, self.correo, self.mensaje)
