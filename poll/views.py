from django.views.generic import DetailView

from .models import *


class PollDetail(DetailView):
    model = Poll
    template_name = 'poll/detail.html'
    context_object_name = 'poll'
