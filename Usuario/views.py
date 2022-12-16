from django.shortcuts import render
from .forms import *
from django.http import HttpResponse
from .models import *

# Create your views here.
def register(request):
    if request.method=="POST":
        form=RegistroUsuarioForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            print (username)
            form.save()
            #aca se podria loguear el usuario, con authenticate y login... pero no lo hago
            return render(request, "padre.html", {"mensaje":f"Usuario {username} creado correctamente"})
        else:
            return render(request, "registrousuario.html", {"form":form, "mensaje":"Error al crear el usuario"})
        
    else:
        form=RegistroUsuarioForm()
        return render(request, "registrousuario.html", {"form":form})
    
def pruebar(request):
    return render(request, "registrousuario.html")
