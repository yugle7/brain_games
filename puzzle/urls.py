from django.urls import path

from .views import *

urlpatterns = [
    path('', PuzzleList.as_view(), name='puzzle-list'),
    path('create/', PuzzleCreate.as_view(), name='puzzle-create'),
    path('<slug:slug>/', PuzzleDetail.as_view(), name='puzzle-detail'),
]
