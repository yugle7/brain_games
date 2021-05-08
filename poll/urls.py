from django.urls import path

from .views import *

urlpatterns = [
    path('', ShowPoll.as_view(), name='show_poll'),
]