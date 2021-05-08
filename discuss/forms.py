from django import forms
from django.core.exceptions import ValidationError

from .models import *


class AddDiscussForm(forms.ModelForm):
    class Meta:
        model = Discuss
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


class GetDiscussForm(forms.ModelForm):
    class Meta:
        model = Filter
        fields = ['query', 'category', 'solved', 'author', 'approved', 'sort_by', 'sort_as']
