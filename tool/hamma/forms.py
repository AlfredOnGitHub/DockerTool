from django import forms
from hamma.models import Usuario
from django.contrib.auth.models import User

class Formulario(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    
    class Meta():
        model = User
        fields = ('username','password','email')

class Usuario(forms.ModelForm):
     
    class Meta():
        model = Usuario
        fields = ('portfolio_site','profile_pic')