from django.shortcuts import render
from .forms import *
from django.http import HttpResponse
from .models import *

# Create your views here.
def register(request):
<<<<<<< HEAD
=======
   
>>>>>>> f3a079c234c639e1c711e4ab70d616b07e2d0ec6
    if request.method=="POST":
        form=RegistroUsuarioForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
<<<<<<< HEAD
            print (username)
=======
>>>>>>> f3a079c234c639e1c711e4ab70d616b07e2d0ec6
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
