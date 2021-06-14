from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView

from solution.forms import SolutionCreateForm
from .models import *


class SolutionDetail(DetailView):
    model = Solution
    template_name = 'solution/detail.html'
    context_object_name = 'solution'


class SolutionList(ListView):
    model = Solution
    template_name = 'solution/list.html'
    context_object_name = 'solutions'

    def get_queryset(self):
        params = {
            'is_submitted': True,
        }
        if 'author' in self.kwargs:
            params['author__login'] = self.kwargs['author']
        if 'is_accepted' in self.kwargs:
            params['is_accepted'] = self.kwargs['is_accepted']

        if 'puzzle' in self.kwargs:
            params['puzzle__slug'] = self.kwargs['puzzle']
        elif 'category' in self.kwargs:
            params['puzzle__category__slug'] = self.kwargs['category']

        return Solution.objects.filter(**params).select_related('author', 'puzzle')


class SolutionCreate(LoginRequiredMixin, CreateView):
    form_class = SolutionCreateForm
    template_name = 'solution/create.html'
    success_url = reverse_lazy('puzzle-detail')
    raise_exception = True
