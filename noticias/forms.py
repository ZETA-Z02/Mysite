from django import forms
from .models import *

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = [
            'nombreu',
            'correo',
            'mensaje',
            'telefono',
        ]

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = [
            'tipodoc',
            'documento',
            'nombres',
            'apellidos',
            'image',
            'pais',
            'estado',
            'correo',
            'telefono',
        ]

class TipoNoticiaForm(forms.ModelForm):
    class Meta:
        model = TipoNoticia
        fields = [
            'tipo',
            'descripcion',
        ]

class NoticiaForm(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = [
            'titulo',
            'descripcion',
            'autor',
            'tipo',
        ]
