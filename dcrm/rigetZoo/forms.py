from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django import forms
from django.forms.widgets import PasswordInput, TextInput
from .models import ZooUser

class CreateUserForm(UserCreationForm):

    class Meta:
        model = ZooUser
        fields = ['username' , 'password1', 'password2']

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())