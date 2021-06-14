from django import forms

from .models import *


class CommentCreateForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
        }
