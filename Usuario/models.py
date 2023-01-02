from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Avatar(models.Model):
    imagen=models.ImageField(upload_to='media/avatares')
    user=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} - {self.imagen}"

class InfoExtra(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=200)
    facebook = models.URLField(max_length=200)
    twitter = models.URLField(max_length=200)
    linkedin = models.URLField(max_length=200)