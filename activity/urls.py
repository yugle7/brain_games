from django.urls import path

from .views import *

urlpatterns = [
    path('', ActivityList.as_view(), name='activity-list'),
]
