from django.urls import path
from Blog.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("crearpost/", crear_post, name="_crearpost"),
    path("post/<id>", post, name="_post"),
    path("buscar_post/", buscar_post, name="_buscarpost"),
    path("editar_post/<id>", editar_post, name="_editarpost"),
    path("eliminar_post/<id>", eliminar_post, name="_eliminarpost"),
    path("buscar_categoria/", buscar_categoria, name="_buscarcategoria"),
    path("sobrenosotros/", sobre_nosotros, name="_sobrenosotros"),
]