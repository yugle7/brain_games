from django import forms

from .models import *


class GetFilterForm(forms.ModelForm):
    class Meta:
        model = Filter
        fields = ['sort_by', 'sort_as', 'is_friend', 'role']
