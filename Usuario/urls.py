from django.urls import path
from Usuario.views import *
from django.contrib.auth.views import LogoutView
from Blog.urls import *

urlpatterns = [
    path("registro/", register, name="_registro"),
    path("ingreso/", login_request, name="_ingreso"),
    path('logout/', LogoutView.as_view(template_name='index.html'), name='_logout'),
    path('perfil/<id>', perfil, name='_perfil'),
    path('editar/', editarPerfil, name="_editar"),
    path('newavatar/', agregarAvatar, name="_newavatar")

]