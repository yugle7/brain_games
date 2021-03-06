from django import forms

from .models import *


class PuzzleCreateForm(forms.ModelForm):
    class Meta:
        model = Puzzle
        fields = ['title', 'slug', 'text']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'text': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
        }


class PuzzleListForm(forms.ModelForm):
    SORT_BY = (
        (1, 'weight'),
        (2, 'create_time'),
        (3, 'solved_count'),
        (4, 'interest'),
        (5, 'complexity'),
    )

    sort_by = forms.ChoiceField(choices=SORT_BY, label="Сортировать по")
    sort_as = forms.BooleanField(label="Сортировать как")

    is_solved = forms.BooleanField(label="Зачтена")
    is_published = forms.BooleanField(label="Опубликована")

    class Meta:
        model = Puzzle
        fields = ['author', 'search', 'category', 'is_solved', 'is_published', 'sort_by', 'sort_as']
