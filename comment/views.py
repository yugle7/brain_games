from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import CommentCreateForm


class CommentCreate(LoginRequiredMixin, CreateView):
    form_class = CommentCreateForm
    template_name = 'comment/create.html'
    raise_exception = True



