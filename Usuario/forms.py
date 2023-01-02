
from django import forms
from django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth.models import User

from Usuario.models import InfoExtra

class RegistroUsuarioForm(UserCreationForm):
    #estoy cambiando el usercreationform por uno propio
    username= forms.CharField(label="Usuario", max_length=50)
    email = forms.EmailField(label="Email")
    password1= forms.CharField(label="Ingrese Contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label="Repita Contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        help_texts = {f: "" for f in fields} #para cada uno de los campos del formulario, le asigna un valor vacio


class AvatarForm(forms.Form):
    imagen=forms.ImageField(label="Imagen")

class UserEditForm(UserCreationForm):
    email = forms.EmailField(label="Email")
    first_name=forms.CharField(label='Nombre')
    last_name=forms.CharField(label='Apellido')
    descripcion = forms.CharField(max_length=200, label="Descripcion")
    facebook = forms.URLField(max_length=200)
    twitter = forms.URLField(max_length=200)
    linkedin = forms.URLField(max_length=200)

    class Meta:
        model = User 
        fields = ['email', 'first_name', 'last_name']
        help_texts = {k:"" for k in fields} 

    def __init__(self, *args, **kargs):
        campo_email = kargs.pop('email',None)
        campo_first_name = kargs.pop('first_name',None)
        campo_last_name = kargs.pop('last_name',None)
        campo_descripcion = kargs.pop('descripcion',None)
        campo_facebook = kargs.pop('facebook',None)
        campo_twitter = kargs.pop('twitter',None)
        campo_linkedin = kargs.pop('linkedin',None)

        super(UserEditForm,self).__init__(*args,**kargs)
        self.fields["email"].initial = campo_email
        self.fields["first_name"].initial = campo_first_name
        self.fields["last_name"].initial = campo_last_name
        self.fields["descripcion"].initial = campo_descripcion
        self.fields["facebook"].initial = campo_facebook
        self.fields["twitter"].initial = campo_twitter
        self.fields["linkedin"].initial = campo_linkedin
        del self.fields['password1']
        del self.fields['password2']

        #super(UserEditForm, self).__init__(*args, **kargs)
        #del self.fields['password1']
        #del self.fields['password2']

        


class PasswordEditForm(UserCreationForm):
    password_antiguo = forms.CharField(label="Contraseña Actual",widget=forms.PasswordInput)
    password1= forms.CharField(label="Nueva Contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label="Repita Contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['password1', 'password2']
        help_texts = {k:"" for k in fields} 


class InfoExtraForm(forms.Form):
    descripcion = forms.CharField(max_length=200, label="Descripcion")
    facebook = forms.URLField(max_length=200)
    twitter = forms.URLField(max_length=200)
    linkedin = forms.URLField(max_length=200)
