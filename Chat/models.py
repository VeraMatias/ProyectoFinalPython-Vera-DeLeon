from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Mensaje(models.Model):
    emisor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='emisor')
    receptor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receptor')
    mensaje = models.CharField(max_length=1500)
    fecha = models.DateTimeField(auto_now_add=True)
    leido = models.BooleanField(default=False)

    class Meta:
        ordering = ('fecha',)



