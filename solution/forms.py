from django import forms

from .models import *


class SolutionCreateForm(forms.ModelForm):
    class Meta:
        model = Puzzle
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
        }

