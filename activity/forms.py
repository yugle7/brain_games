from django import forms

from .models import *


class ActivityListForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = ['tags', 'author', 'search']
