from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import FormMixin

from poll.forms import PollListForm
from .models import *


class PollDetail(DetailView):
    model = Poll
    template_name = 'poll/detail.html'
    context_object_name = 'poll'


class PollList(FormMixin, ListView):
    model = Poll

    template_name = 'poll/list.html'
    context_object_name = 'polls'
    form_class = PollListForm

    def get_success_url(self):
        return reverse_lazy('poll-list')

    def get_queryset(self):
        return Poll.objects.all()
