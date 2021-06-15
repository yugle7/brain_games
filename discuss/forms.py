from django import forms

from .models import *


class DiscussCreateForm(forms.ModelForm):
    class Meta:
        model = Discuss
        fields = ['title', 'slug', 'text']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'text': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
        }


class DiscussListForm(forms.ModelForm):
    class Meta:
        model = Discuss
        fields = ['author', 'topic', 'search']

