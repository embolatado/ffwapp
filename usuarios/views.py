from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UsuarioRegistroForm

# Create your views here.

def registro(request):
    if request.method == "POST":
        # RECREA UN FORM CON LA INFO PASADA EN `POST` EN CASO ERROR
        formulario = UsuarioRegistroForm(request.POST)

        if formulario.is_valid():
            formulario.save()
            usrnme = formulario.cleaned_data.get('username')
            # FLASH MESSAGES CON f' NOTATION
            messages.success(request, f'¡Cuenta, {usrnme} creada con éxito!')
            
            return redirect('blog-inicio')
    else:
        formulario = UsuarioRegistroForm() # RETORNA EL FORMULARIO VACÍO
    
    # CUANDO EL NO HA SIDO DETECTADO UN METHOD
    return render(request, "usuarios/registro.html", {'form_reg': formulario})
