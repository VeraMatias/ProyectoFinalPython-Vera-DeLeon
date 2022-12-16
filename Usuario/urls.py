from django.urls import path
from Usuario.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("registro/", register, name="_registro"),

]