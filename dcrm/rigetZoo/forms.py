from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django import forms
from django.forms.widgets import PasswordInput, TextInput
from .models import ZooUser, zooBooking, hotelBooking

class CreateUserForm(UserCreationForm):

    class Meta:
        model = ZooUser
        fields = ['first_name', 'last_name', 'email','houseNum','street','postCode','phoneNum','username','password1','password2']
        labels = {
            'first_name': "First Name",
            'last_name':"Last Name",
            'email':'Email',
            'houseNum': 'House Number or Name',
            'street':"Street",
            'postCode':'Post Code',
            'phoneNum': 'Phone Number',
        }

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())

class bookZooForm(forms.ModelForm):

    class Meta:
        model = zooBooking
        fields = ["dateStart","dateEnd","adult","child","price"]
        labels={
            "dateStart": "Enter your starting date",
            "dateEnd": "Enter when you want to finish",
            "adult":"How many adults?",
            "child":"How many children?"
        }
        widgets = {
            'dateStart':forms.DateInput(attrs={'type':'date'}),
            'dateEnd':forms.DateInput(attrs={'type':'date'}),
            'price':forms.HiddenInput(),
        }