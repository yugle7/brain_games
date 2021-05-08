from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, ListView

from puzzle.forms import *
from puzzle.models import *


class ShowPuzzle(DetailView):
    model = Puzzle
    template_name = 'puzzle/show.html'
    context_object_name = 'puzzle'


class PuzzleList(ListView):
    model = Puzzle
    template_name = 'puzzle/list.html'
    context_object_name = 'puzzles'

    def get_queryset(self):
        puzzles = Puzzle.objects.filter(published=True).select_related('author', 'category')

        if 'author' in self.kwargs:
            puzzles = puzzles.filter(author__login=self.kwargs['author'])

        if 'approved' in self.kwargs:
            puzzles = puzzles.filter(approved=self.kwargs['approved'])

        if 'category' in self.kwargs:
            puzzles = puzzles.filter(category__slug=self.kwargs['category'])

        return puzzles


class AddPuzzle(LoginRequiredMixin, CreateView):
    form_class = AddPuzzleForm
    template_name = 'puzzle/add.html'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('home')
    raise_exception = True
