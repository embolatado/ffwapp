from django.shortcuts import render
from .models import Post

# Create your views here.

def inicio(request):
    contexto = {"publicaciones": Post.objects.all()}
    return render(request, 'blog/inicio.html', contexto)


def acerca(request):
    return render(request, 'blog/about.html', {'titulo': "Acerca de Blog"})
