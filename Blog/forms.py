from typing import Any
from django import forms
from ckeditor.fields import RichTextFormField

class PostForm(forms.Form):
    titulo = forms.CharField(max_length=20)
    subtitulo = forms.CharField(max_length=50)
    cuerpo = RichTextFormField()
    imagen = forms.ImageField(label="Imagen")

    Categorias = (
    ("FUTBOL", "Futbol"),
    ("JUEGOS", "Juegos"),
    ("VIAJES", "Viajes"),
    ("SALUD", "Salud"),
    ("EVENTOS", "Eventos"),
    ("VARIOS", "Varios"),
    )

    categoria = forms.ChoiceField(choices = Categorias)

class PostEditForm(forms.Form):
    titulo = forms.CharField(max_length=20)
    subtitulo = forms.CharField(max_length=50)
    cuerpo = RichTextFormField()
    imagen = forms.ImageField(label="Imagen", required=False)

    Categorias = (
    ("FUTBOL", "Futbol"),
    ("JUEGOS", "Juegos"),
    ("VIAJES", "Viajes"),
    ("SALUD", "Salud"),
    ("EVENTOS", "Eventos"),
    ("VARIOS", "Varios"),
    )

    categoria = forms.ChoiceField(choices = Categorias)

