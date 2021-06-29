from django.urls import path

from .views import *

urlpatterns = [
    path('', DiscussList.as_view(), name='discuss-list'),
    path('create/', DiscussCreate.as_view(), name='discuss-create'),
    path('<slug:slug>/', DiscussDetail.as_view(), name='discuss-detail'),
]
