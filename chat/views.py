from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.views.generic.edit import FormMixin

from person.models import Person
from .forms import AddCommentForm
from .models import Comment


def comment_like(request):
    comment = Comment.objects.get(pk=request.GET['pk'])
    if comment.author.username == request.user.username:
        comment.is_liked = not comment.is_liked
        comment.save()


def comment_hide(request):
    comment = Comment.objects.get(pk=request.GET['pk'])
    if comment.author.username == request.user.username:
        comment.is_hidden = not comment.is_hidden
        comment.save()


class ShowChat(FormMixin, DetailView):
    model = Person
    template_name = 'chat/show.html'
    context_object_name = 'person'
    form_class = AddCommentForm

    def get_success_url(self):
        pk = self.get_object().pk
        return reverse_lazy('show_person', kwargs={'pk': pk})

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        return self.form_valid(form) if form.is_valid() else self.form_invalid(form)

    def form_valid(self, form):
        comment = form.save(commit=False)
        print(self.request.user)
        comment.author = self.request.user
        comment.person = self.get_object()
        comment.save()
        return super().form_valid(form)
