from django.urls import path
from Chat.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("inicio", inicio, name="_iniciochat"),
    path("nuevochat", nuevochat, name="_nuevochat"),
    path("enviarmsj", enviarmsj, name="_enviarmsj"),

]