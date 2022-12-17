from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField 

# Create your models here.

class Post(models.Model):
    titulo = models.CharField(max_length=20)
    subtitulo = models.CharField(max_length=50)
    cuerpo = RichTextField(verbose_name="Contenido")
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateField()
    imagen = models.ImageField(upload_to='media')

    Categorias = (
    ("FUTBOL", "Futbol"),
    ("JUEGOS", "Juegos"),
    ("VIAJES", "Viajes"),
    ("SALUD", "Salud"),
    ("EVENTOS", "Eveentos"),
    ("VARIOS", "Varios"),
    )

    categoria = models.CharField(max_length=9, choices=Categorias, default="VARIOS")
