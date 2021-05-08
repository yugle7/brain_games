from django.views.generic import DetailView

from .models import *


class ShowPoll(DetailView):
    model = Poll
    template_name = 'poll/show.html'
    context_object_name = 'poll'
