from django.shortcuts import render
from .forms import *
from .models import Post
from datetime import datetime
from django.core.paginator import Paginator

# Create your views here.

def inicio(request):

        post = Post.objects.all().order_by('-fecha')
        paginator = Paginator(post, 6)

        numero_pagina = request.GET.get('page')
        post_por_pagina = paginator.get_page(numero_pagina)
        return render (request, "index.html", {"post_pagina": post_por_pagina})

def crear_post(request):
    if request.method=="POST":
        form=PostForm(request.POST, request.FILES)
        if form.is_valid():
            informacion=form.cleaned_data
            print(informacion)

            Post_a_Cargar=Post(titulo=informacion["titulo"],subtitulo=informacion["subtitulo"], cuerpo= informacion["cuerpo"], autor =request.user,fecha = datetime.now(),imagen=request.FILES["imagen"], categoria = informacion["categoria"])

            Post_a_Cargar.save()
            return render (request, "index.html")
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
