from django import forms

from .models import *


class SolutionCreateForm(forms.ModelForm):
    class Meta:
        model = Solution
        fields = ['answer']
        widgets = {
            'answer': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
        }


class SolutionListForm(forms.ModelForm):
    class Meta:
        model = Solution
        fields = ['person', 'puzzle', 'is_submitted', 'is_accepted', 'category']
