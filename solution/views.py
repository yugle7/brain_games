from django.views.generic import DetailView

from .models import *


class ShowSolution(DetailView):
    model = Solution
    template_name = 'solution/show.html'
    context_object_name = 'solution'
