from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.

posts = [
    {
        "titulo": "Primer post de blog",
        "contenido": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do.",
        "autor": "Juan Díaz",
        "fecha_publicado": "6 de mayo de 2021"
    },
    {
        "titulo": "Segunda publicación de blog",
        "contenido": "Eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation.",
        "autor": "María López",
        "fecha_publicado": "8 de mayo de 2021"
    }
]


def inicio(request):
    contexto = {"publicaciones": posts}
    return render(request, 'blog/inicio.html', contexto)


def acerca(request):
    return render(request, 'blog/about.html', {'titulo': "Acerca de Blog"})
