from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import FormMixin

from activity.forms import ActivityListForm
from .models import *


class ActivityList(FormMixin, ListView):
    model = Activity

    template_name = 'activity/list.html'
    context_object_name = 'activities'
    form_class = ActivityListForm

    def get_success_url(self):
        return reverse_lazy('activity-list')

    def get_queryset(self):
        return Activity.objects.all()
