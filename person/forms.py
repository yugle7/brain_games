from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import *


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


class PersonListForm(forms.Form):
    SORT_BY = (
        (1, 'rating'),
        (2, 'contribution'),
        (3, 'money'),
        (4, 'last_visit_time'),
        (5, 'date_joined'),
    )
    sort_by = forms.ChoiceField(choices=SORT_BY, label="Сортировать по")
    sort_as = forms.BooleanField(label="Сортировать как")

    is_friend = forms.BooleanField(label="Друг")

    role = forms.CharField(max_length=MAX_SLUG_LEN, label="Роль")
    search = forms.CharField(max_length=MAX_QUERY_LEN, label="Поисковый запрос")
