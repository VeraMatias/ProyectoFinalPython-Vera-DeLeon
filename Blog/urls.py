from django.urls import path
from Blog.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("crearpost/", crear_post, name="_crearpost"),

]