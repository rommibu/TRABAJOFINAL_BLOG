from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from AppMVT.models import User
from django.contrib.auth.models import User
#importo la libreria
from django.forms import ModelForm
from .models import *
from .models import Post


class FormularioFamilia(forms.Form):
    nombre=forms.CharField(max_length=60)
    apellido=forms.CharField(max_length=60)
    dni=forms.FloatField()
    extranjero=forms.BooleanField()
    enfermedadbase=forms.CharField(max_length=20)
    mail=forms.EmailField()

class FormularioTrabajo(forms.Form):
    empresa=forms.CharField(max_length=60)
    antiguedad= forms.IntegerField()
    profesion=forms.CharField(max_length=50)
    contrato=forms.CharField(max_length=60)
    
    
#Agrego el form para la vista de la eleccion de la escuderia

#formulario escuderia       
class AutosFormu(ModelForm):
    class Meta:
        model = Autos
        fields = "__all__"

class UserRegisterForm(UserCreationForm):
    email=forms.EmailField()
    password1=forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2=forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        labels = {'username': 'Nombre completo', 'email': 'Agrega tu mail'}
        help_texts = {k:" " for k in fields}

class AutenticarForm(forms.ModelForm):
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'password')

"""class clean(self):
    email = self.cleaned_data['email']
    password = self.cleaned_data['password']

    if not authenticate(email=email, password=password):
        raise forms.ValidationError("El mail o contraseña son incorrectos")"""

class AvatarForm(forms.Form):
    imagen= forms.ImageField(label="Imagen")


class UserEditForm(UserCreationForm):
    email=forms.EmailField(label='Modificar E-mail')
    password1=forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2=forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput)
    firstName=forms.CharField(label='Modificar Nombre')
    lastName=forms.CharField(label='Modificar Apellido')

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'first_name', 'last_name']
        help_texts = {k:"" for k in fields}

class AvatarForm(forms.Form):
    imagen= forms.ImageField(label="Imagen")

class PostForm(forms.ModelForm):
    content=forms.CharField(label='', widget=forms.Textarea(attrs={'row':2, 'placeholder': 'Que esta pasando?'}))

    class Meta:
        model = Post
        fields = ['content']
        