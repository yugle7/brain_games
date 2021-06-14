from django.urls import path

from .views import *

urlpatterns = [
    path('', PollDetail.as_view(), name='poll-detail'),
]