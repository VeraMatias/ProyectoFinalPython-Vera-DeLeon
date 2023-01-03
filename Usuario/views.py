from django.shortcuts import redirect, render

from Blog.models import Post
from .forms import *
from .models import *

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.hashers import check_password

from django.contrib.auth.decorators import login_required


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

            return redirect('/')
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
                return redirect('/')
            else:
                return redirect('/')

        else:
            return render(request, 'ingresousuario.html', {'mensaje':"Usuario o contraseña incorrectos", 'form':form})

    else:
        form = AuthenticationForm()
    return render(request, "ingresousuario.html", {"form":form})


def perfil(request,id):
    usuario=User.objects.get(id=id)
    posteos=Post.objects.filter(autor=usuario).order_by('-fecha')
    info_extra = ""
    try:
        info_extra=InfoExtra.objects.get(usuario_id = usuario.id)
    except:
        pass

    lista=Avatar.objects.filter(user=usuario)
    if len(lista)!=0:
        imagen=lista[0].imagen.url
    else:
        imagen="../../media/avatares/avatarpordefecto.png"

    if info_extra is not None:
        return render(request, "perfil.html",{"usuario": usuario, "perfil_avatar":imagen, "posteos":posteos, "info_extra":info_extra})
    else:
        return render(request, "perfil.html",{"usuario": usuario, "perfil_avatar":imagen, "posteos":posteos})

@login_required
def editar_avatar(request):
    if request.method=="POST":
        form=AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            avatarViejo=Avatar.objects.filter(user=request.user)
            if len(avatarViejo)!=0:
                avatarViejo[0].delete()
            avatar=Avatar(user=request.user, imagen=request.FILES["imagen"])
            avatar.save()
            return render(request, "perfil.html",{"usuario": request.user, "perfil_avatar":avatar.imagen.url})
        else:
            return render(request, "editaravatar.html", {"formulario": form, "usuario": request.user})
    else:
        form=AvatarForm()
        return render(request , "editaravatar.html", {"formulario": form, "usuario": request.user})

@login_required
def editar_perfil(request):
    usuario=request.user
    info_extra = ""

    try:
        info_extra=InfoExtra.objects.get(usuario_id = usuario.id)
    except:
        pass

    if request.method=="POST":
        form=UserEditForm(request.POST)
        if form.is_valid():
            #Informacion en modelo User
            info=form.cleaned_data
            usuario.email=info["email"]
            usuario.first_name=info["first_name"]
            usuario.last_name=info["last_name"]
            usuario.save()

            #Informacion en modelo InfoExtra
            if info_extra != "" :
                info_extra.usuario = request.user
                info_extra.descripcion=info["descripcion"]
                info_extra.facebook=info["facebook"]
                info_extra.twitter=info["twitter"]
                info_extra.linkedin=info["linkedin"]
                info_extra.save()
            else:
                info_a_crear = InfoExtra(usuario = usuario, descripcion=info["descripcion"], facebook=info["facebook"], twitter=info["twitter"],linkedin=info["linkedin"] )
                info_a_crear.save()

            #Obtencion de avatar para render
            lista=Avatar.objects.filter(user=usuario)
            if len(lista)!=0:
                imagen=lista[0].imagen.url
            else:
                imagen="../../media/avatares/avatarpordefecto.png"

            #Obtencion de posteos para render
            posteos=Post.objects.filter(autor=usuario).order_by('-fecha')

            return render(request, "perfil.html",{"usuario": request.user, "perfil_avatar":imagen, "info_extra":info_extra, "posteos":posteos})
        else:
            return render(request, "editarusuario.html", {"form": form, "usuario": request.user})
    else:
        if info_extra != "":
            form=UserEditForm(email = usuario.email, first_name = usuario.first_name, last_name=usuario.last_name, descripcion = info_extra.descripcion, facebook = info_extra.facebook, twitter=info_extra.twitter, linkedin = info_extra.linkedin)
        else:
            form=UserEditForm(email = usuario.email, first_name = usuario.first_name, last_name=usuario.last_name)
        return render(request, "editarusuario.html", {"form": form, "usuario": request.user}) 

@login_required
def editar_password(request):
    usuario=request.user
    if request.method=="POST":
        form=PasswordEditForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            if check_password(info["password_antiguo"],request.user.password):
                usuario.set_password(info["password1"])
                usuario.save()

                #Obtencion de avatar para render
                lista=Avatar.objects.filter(user=usuario)
                if len(lista)!=0:
                    imagen=lista[0].imagen.url
                else:
                    imagen="../../media/avatares/avatarpordefecto.png"

                #Obtencion de posteos para render
                posteos=Post.objects.filter(autor=usuario).order_by('-fecha')
                return render(request, "perfil.html",{"usuario": request.user, "perfil_avatar":imagen, "posteos":posteos})
            else:
                return render(request, "editarpassword.html", {"form": form, "usuario": request.user, "mensaje": "Password actual incorrecto"})
        else:
            return render(request, "editarpassword.html", {"form": form, "usuario": request.user, "mensaje": "Error"})
    else:
        form=PasswordEditForm()
        return render(request, "editarpassword.html", {"form": form, "usuario": request.user}) 


