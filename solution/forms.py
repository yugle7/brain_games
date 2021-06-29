from django import forms

from .models import *


class SolutionListForm(forms.Form):
    class Meta:
        model = Solution
        fields = ['solver', 'puzzle', 'is_accepted']
