from django import forms
from django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth.models import User

class RegistroUsuarioForm(UserCreationForm):
    #estoy cambiando el usercreationform por uno propio
    f_nombre= forms.CharField(label="Nombre de Usuario", max_length=50)
    f_email = forms.EmailField(label="Email")
    password1= forms.CharField(label="Ingrese Contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label="Repita Contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["f_nombre", "f_email", "password1", "password2"]
        help_texts = {f: "" for f in fields} #para cada uno de los campos del formulario, le asigna un valor vacio