from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import *


class GetFilterForm(forms.ModelForm):
    class Meta:
        model = Filter
        fields = ['sort_by', 'sort_as', 'is_friend', 'role']


class RegisterUserForm(UserCreationForm):
    username = forms.SlugField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = Person
        fields = ('username', 'email', 'password')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
