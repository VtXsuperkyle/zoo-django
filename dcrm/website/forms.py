from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import zoo_user
from django import forms
from django.forms.widgets import PasswordInput, TextInput

from .models import zoo_user

# - Register or create a user
class CreateUserForm(UserCreationForm):

    class Meta:
        model = zoo_user
        fields = ['username', 'password1', 'password2']


# - login user
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())

# - add record
class CreationRecordForm(forms.ModelForm):
    class Meta:
        model = zoo_user
        fields = ['first_name', 'last_name', 'email', 'phone', 'address','city']