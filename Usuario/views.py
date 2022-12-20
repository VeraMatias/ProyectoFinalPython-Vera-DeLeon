from django.shortcuts import render
from .forms import *
from django.http import HttpResponse
from .models import *
#from Blog.views import inicio

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate

#from django.urls import reverse_lazy


# Create your views here.
def register(request):
    if request.method=="POST":
        form=RegistroUsuarioForm(request.POST)
        if form.is_valid():
            
            form.save()

            username=form.cleaned_data.get("username")
            
            clave=form.cleaned_data.get("password1")

            usuario=authenticate(username=username, password=clave)    
            login(request, usuario)

            
            #aca se podria loguear el usuario, con authenticate y login... pero no lo hago
            return render(request, "index.html", {"mensaje":f"Usuario {username} creado correctamente"})
        else:
            return render(request, "registrousuario.html", {"form":form, "mensaje":"Error al crear el usuario"})
        
    else:
        form=RegistroUsuarioForm()
        return render(request, "registrousuario.html", {"form":form})
    
def login_request(request):
    if request.method == "POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usu=form.cleaned_data.get("username")
            clave=form.cleaned_data.get("password")

            usuario=authenticate(username=usu, password=clave)#trae un usuario de la base, que tenga ese usuario y ese pass, si existe, lo trae y si no None
            if usuario is not None:    
                login(request, usuario)
                return render(request, 'index.html', {'mensaje':f"Bienvenido {usuario}" })
            else:
                return render(request, 'index.html', {'mensaje':"Usuario o contraseña incorrectos", 'form':form})

        else:
            return render(request, 'ingresousuario.html', {'mensaje':"Usuario o contraseña incorrectos", 'form':form})

    else:
        form = AuthenticationForm()
    return render(request, "ingresousuario.html", {"form":form})



def obtenerAvatar(request):
    lista=Avatar.objects.filter(user=request.user)
    if len(lista)!=0:
        imagen=lista[0].imagen.url
    else:
        imagen="media/avatares/avatarpordefecto.png"
    return imagen


def perfil(request):
    return render(request, "perfil.html")