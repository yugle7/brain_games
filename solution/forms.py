from django import forms

from .models import *


class SolutionListForm(forms.ModelForm):
    class Meta:
        model = Solution
        fields = ['author', 'puzzle', 'is_accepted']
