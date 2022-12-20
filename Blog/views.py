from django.shortcuts import render
from .forms import *
from Usuario.models import Avatar
from Usuario.views import obtenerAvatar
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate

# Create your views here.

#@login_required
def inicio(request):
    if request.user.is_authenticated:
        lista=Avatar.objects.filter(user=request.user)
        return render (request, "index.html", {"imagen":obtenerAvatar(request)})
        
    else:
        return render (request, "index.html")
   
    

def crear_post(request):
    if request.method=="POST":
        pass
    else:
        form=PostForm()
        return render(request , "crear_post.html", {"form": form, "usuario": request.user})
    return render(request, "crear_post.html")
