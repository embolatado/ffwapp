from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=90, verbose_name="título")
    content = models.TextField(verbose_name="contenido")
    date_posted = models.DateTimeField(default=timezone.now, verbose_name="creado")
    last_update = models.DateTimeField(auto_now=True, verbose_name="modificado")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="por")

    def __str__(self):
        return self.title



