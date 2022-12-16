from django.urls import path
from Usuario.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("registro/", register, name="_registro"),
    path("ingreso/", login_request, name="_ingreso"),
    path('logout/', LogoutView.as_view(), name='_logout'),

]