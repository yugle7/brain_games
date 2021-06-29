from django.views.generic import DetailView, ListView
from django.views.generic.edit import FormMixin

from solution.forms import SolutionListForm
from .models import *


class SolutionDetail(DetailView):
    model = Solution
    template_name = 'solution/detail.html'
    context_object_name = 'solution'


class SolutionList(FormMixin, ListView):
    model = Solution
    template_name = 'solution/list.html'
    context_object_name = 'solutions'
    form_class = SolutionListForm

    def get_queryset(self):
        params = {}

        if 'solver' in self.kwargs:
            params['solver__login'] = self.kwargs['solver']
        if 'is_accepted' in self.kwargs:
            params['is_accepted'] = self.kwargs['is_accepted']

        if 'puzzle' in self.kwargs:
            params['puzzle__slug'] = self.kwargs['puzzle']
        elif 'category' in self.kwargs:
            params['puzzle__category__slug'] = self.kwargs['category']

        return Solution.objects.filter(**params).select_related('solver', 'puzzle')
