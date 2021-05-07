from django.urls import path
from .views import inicio, acerca

urlpatterns = [
    path('', inicio, name="blog-inicio"),
    path('about/', acerca, name="blog-about"),
]