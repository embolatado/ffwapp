from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db.models.deletion import CASCADE

# Create your models here.

class Perfil(models.Model):
    usr = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(default="nadie.png", upload_to='img_perfiles')

    class Meta:
        verbose_name = "perfil"
        verbose_name_plural = "perfiles"
        
    def __str__(self):
        return f'Perfil de {self.usr.username}'
