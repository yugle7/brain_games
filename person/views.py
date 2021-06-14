from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.views.generic import CreateView
from django.views.generic import ListView, DetailView

from .forms import *


class PersonList(ListView):
    model = Person
    template_name = 'person/list.html'
    context_object_name = 'persons'


class PersonDetail(DetailView):
    model = Person
    template_name = 'person/detail.html'
    context_object_name = 'person'


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'person/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        person = form.save()
        login(self.request, person)

        return reverse_lazy(self.request.GET.get('next', 'puzzle_list'))


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'person/login.html'

    def get_success_url(self):
        return reverse_lazy(self.request.GET.get('next', 'puzzle_list'))


def logout_user(request):
    logout(request)
    return redirect('home')
