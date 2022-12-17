from django.shortcuts import render
from .forms import *

# Create your views here.

def inicio(request):
    return render(request, "index.html")

def crear_post(request):
    if request.method=="POST":
        pass
    else:
        form=PostForm()
        return render(request , "crear_post.html", {"form": form, "usuario": request.user})
    return render(request, "crear_post.html")
