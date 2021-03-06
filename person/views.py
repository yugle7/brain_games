from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin

from .forms import *


class PersonList(ListView, FormMixin):
    model = Person

    template_name = 'person/list.html'
    context_object_name = 'persons'
    form_class = PersonListForm

    def get_success_url(self):
        return reverse_lazy('person-list')

    def get_queryset(self):
        return Person.objects.all()

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        return self.form_valid(form) if form.is_valid() else self.form_invalid(form)

    def form_valid(self, form):
        return super().form_valid(form)


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

        return reverse_lazy(self.request.GET.get('next', 'puzzle-list'))


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'person/login.html'

    def get_success_url(self):
        return reverse_lazy(self.request.GET.get('next', 'puzzle-list'))


def logout_user(request):
    logout(request)
    return redirect('puzzle-list')
