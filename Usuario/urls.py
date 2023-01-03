from django.urls import path
from Usuario.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("registro/", register, name="_registro"),
    path("ingreso/", login_request, name="_ingreso"),
    path('logout/', LogoutView.as_view(next_page='_inicio'), name='_logout'),
    path('perfil/<id>', perfil, name='_perfil'),
    path('editaravatar/', editar_avatar, name="_editaravatar"),
    path('editarperfil/', editar_perfil, name="_editarusuario"),
    path('editarpassword/', editar_password, name="_editarpassword"),
]