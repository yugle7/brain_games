from django.urls import path

from .views import *

urlpatterns = [
    path('', PollList.as_view(), name='poll-list'),
    path('<int:pk>/', PollDetail.as_view(), name='poll-detail'),
]
