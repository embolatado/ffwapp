from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.

def registro(request):
    if request.method == "POST":
        # CREA UN FORM CON LA INFO PASADA EN `POST`
        formulario = UserCreationForm(request.POST)

        if formulario.is_valid():
            usrnme = formulario.cleaned_data.get('username')
            # FLASH MESSAGES
            messages.success(request, f'¡Cuenta, {usrnme} creada con éxito!')
            return redirect('blog-inicio')
    else:
        formulario = UserCreationForm() # RETORNA EL FORMULARIO VACÍO
    
    # CUANDO EL NO HA SIDO DETECTADO UN METHOD
    return render(request, "usuarios/registro.html", {'form_reg': formulario})
