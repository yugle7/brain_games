from django.urls import path, re_path
from django.views.decorators.cache import cache_page

from .views import *

urlpatterns = [
    path('', PuzzleList.as_view(), name='puzzle_list'),
    path('add/', ShowPuzzle.as_view(), name='add_puzzle'),
    path('<slug:slug>/', ShowPuzzle.as_view(), name='show_puzzle'),
]
