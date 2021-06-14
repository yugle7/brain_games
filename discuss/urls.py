from django.urls import path

from .views import *

urlpatterns = [
    path('create/', DiscussCreate.as_view(), name='discuss-create'),
    path('', DiscussList.as_view(), name='discuss-list'),
    path('<slug:slug>/', DiscussDetail.as_view(), name='discuss-detail'),
]
