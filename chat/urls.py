from django.urls import path

from .views import *

urlpatterns = [
    path('like/<int:pk>/', comment_like, name='like_chat_comment'),
    path('hide/<int:pk>/', comment_hide, name='hide_chat_comment'),
]
