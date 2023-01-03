from django.shortcuts import redirect, render
from .forms import *
from .models import Post
from datetime import datetime
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# Create your views here.

def inicio(request):

        post = Post.objects.all().order_by('-fecha')
        paginator = Paginator(post, 6) #(objetos a subdividir, cantidad de muestras por pagina)

        numero_pagina = request.GET.get('page') #obtencion de la pagina
        post_por_pagina = paginator.get_page(numero_pagina) # extraccion de los post de dicha pagina
        return render (request, "index.html", {"post_pagina": post_por_pagina}) 

@login_required
def crear_post(request):
    if request.method=="POST":
        form=PostForm(request.POST, request.FILES)
        if form.is_valid():
            informacion=form.cleaned_data
            Post_a_Cargar=Post(titulo=informacion["titulo"],subtitulo=informacion["subtitulo"], cuerpo= informacion["cuerpo"], autor =request.user,fecha = datetime.now(),imagen=request.FILES["imagen"], categoria = informacion["categoria"])

            Post_a_Cargar.save()
            #return render (request, "index.html")
            return redirect('/')
        else:
            return render(request, "crear_post.html", {"form":form})
    else:
        form=PostForm()
        return render(request , "crear_post.html", {"form": form, "usuario": request.user})


def post(request, id):
    post=Post.objects.get(id=id)
    try:
        imagen=post.imagen.url
    except:
        imagen="/media/defecto.jpg"

    return render (request, "post.html", {"post": post, "imagen": imagen})

def buscar_post(request):
    if request.GET["busq_titulo"]:
        resultado_busqueda=Post.objects.filter(titulo__icontains=request.GET["busq_titulo"]).order_by('-fecha')
        return render(request,"buscar_post.html",{"resultado_busqueda": resultado_busqueda})
    else:
        return render(request, "buscar_post.html")

def buscar_categoria(request):
    if request.GET["categoria"]:
        categoria_recibida = str(request.GET["categoria"])
        resultado_busqueda=Post.objects.filter(categoria=categoria_recibida.upper()).order_by('-fecha')
        return render(request,"buscar_categoria.html",{"resultado_busqueda": resultado_busqueda})
    else:
        return render(request, "buscar_categoria.html")

@login_required
def editar_post(request,id):
    post=Post.objects.get(id=id)
    if (request.user.id == post.autor.id) or request.user.is_superuser:
        if request.method=="POST":

            form=PostEditForm(request.POST, request.FILES)

            if form.is_valid():
                info=form.cleaned_data
                post.titulo=info["titulo"]           
                post.subtitulo=info["subtitulo"]
                post.cuerpo=info["cuerpo"]
                post.categoria = info["categoria"]
                if len(request.FILES) != 0:
                    post.imagen=request.FILES["imagen"]
                post.save()
                return redirect('/')
            else:
                return render(request, "editar_post.html", {"form":form, "mensaje":"Error al editar el post", "post":post})
        else:
            form= PostForm(initial={"titulo":post.titulo, "subtitulo":post.subtitulo, "cuerpo":post.cuerpo, "imagen":post.imagen, "categoria":post.categoria})
            return render(request, "editar_post.html", {"form":form, "post":post})
    else:
        return render(request, "editar_post.html", {"mensaje":"Usted no es el Autor de este Post.", "post":post})

@login_required
def eliminar_post(request, id):
    post=Post.objects.get(id=id)
    if (request.user.id == post.autor.id) or request.user.is_superuser:
        post.delete()
        return redirect('/')
    else:
        return redirect('/')

def sobre_nosotros(request):
    return render(request, "sobrenosotros.html")