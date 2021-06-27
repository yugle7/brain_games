from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView
from django.views.generic import ListView
from django.views.generic.edit import FormMixin

from comment.forms import CommentCreateForm
from discuss.forms import DiscussCreateForm, DiscussListForm
from .models import *


class DiscussList(FormMixin, ListView):
    model = Discuss

    template_name = 'discuss/list.html'
    context_object_name = 'discusses'
    form_class = DiscussListForm

    def get_success_url(self):
        return reverse_lazy('discuss-list')

    def get_queryset(self):
        return Discuss.objects.all()


class DiscussDetail(FormMixin, DetailView):
    model = Discuss
    template_name = 'discuss/detail.html'
    context_object_name = 'discuss'
    form_class = CommentCreateForm

    def get_success_url(self):
        pk = self.get_object().pk
        return reverse_lazy('discuss-detail', kwargs={'pk': pk})

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        return self.form_valid(form) if form.is_valid() else self.form_invalid(form)

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.author = self.request.user
        comment.talk = self.get_object().talk

        if not super().form_valid(form):
            return False

        comment.save()


class DiscussCreate(LoginRequiredMixin, CreateView):
    form_class = DiscussCreateForm
    template_name = 'discuss/create.html'
    success_url = reverse_lazy('discuss-detail')
    raise_exception = True
