from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin

from main.forms import *


class PersonList(ListView):
    model = Person
    template_name = 'person/includes/list.html'
    context_object_name = 'persons'


class ShowPerson(DetailView):
    model = Person
    template_name = 'person/show.html'
    context_object_name = 'person'
