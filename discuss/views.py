from django.views.generic import DetailView, ListView

from .models import *


class ShowDiscuss(DetailView):
    model = Discuss
    template_name = 'discuss/show.html'
    context_object_name = 'discuss'


class DiscussList(ListView):
    model = Discuss
    template_name = 'discuss/list.html'
    context_object_name = 'discusses'

    def get_queryset(self):
        if 'author' in self.kwargs:
            pass
        return Discuss.objects.all()
