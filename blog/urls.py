from django.urls import path
from .views import inicio, acerca
from usuarios.views import registro

urlpatterns = [
    path('', inicio, name="blog-inicio"),
    path('about/', acerca, name="blog-about"),
    path('registro/', registro, name="usuarios-reg"),
]