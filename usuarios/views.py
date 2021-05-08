from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def registro(request):
    formulario = UserCreationForm()
    return render(request, "usuarios/registro.html", {'form_reg': formulario})