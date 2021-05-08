from django import forms
from django.core.exceptions import ValidationError

from .models import *


class AddPuzzleForm(forms.ModelForm):
    class Meta:
        model = Puzzle
        fields = ['title', 'slug', 'text']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'text': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > MAX_TITLE_LEN:
            raise ValidationError(f'Название не более {MAX_TITLE_LEN} символов')

        return title


class GetPuzzlesForm(forms.ModelForm):
    class Meta:
        model = Filter
        fields = ['query', 'category', 'is_solved', 'author', 'is_published', 'sort_by', 'sort_as']
