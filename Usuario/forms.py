from django import forms
from django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth.models import User

class RegistroUsuarioForm(UserCreationForm):
    #estoy cambiando el usercreationform por uno propio
<<<<<<< HEAD
    username= forms.CharField(label="Usuario", max_length=50)
    email = forms.EmailField(label="Email")
=======
    f_nombre= forms.CharField(label="Nombre de Usuario", max_length=50)
    f_email = forms.EmailField(label="Email")
>>>>>>> f3a079c234c639e1c711e4ab70d616b07e2d0ec6
    password1= forms.CharField(label="Ingrese Contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label="Repita Contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
<<<<<<< HEAD
        fields = ["username", "email", "password1", "password2"]
=======
        fields = ["f_nombre", "f_email", "password1", "password2"]
>>>>>>> f3a079c234c639e1c711e4ab70d616b07e2d0ec6
        help_texts = {f: "" for f in fields} #para cada uno de los campos del formulario, le asigna un valor vacio