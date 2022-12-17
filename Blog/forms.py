from django import forms
from ckeditor.widgets import CKEditorWidget
from ckeditor.fields import RichTextFormField

class PostForm(forms.Form):
    titulo = forms.CharField(max_length=20)
    subtitulo = forms.CharField(max_length=50)
    cuerpo = RichTextFormField()
    #autor = ForeignKey(User, on_delete=models.CASCADE)
    fecha = forms.DateField()
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