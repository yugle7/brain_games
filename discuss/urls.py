from django.urls import path

from .views import *

urlpatterns = [
    path('<slug:slug>/', ShowDiscuss.as_view(), name='show_discuss'),
    path('', DiscussList.as_view(), name='discuss_list'),
]
