from django.urls import path

from .views import *

urlpatterns = [
    path('create/', CommentCreate.as_view(), name='comment-create'),
]
