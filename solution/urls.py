from django.urls import path

from .views import *

urlpatterns = [
    path('', SolutionList.as_view(), name='solution-list'),
    path('<int:id>/', SolutionDetail.as_view(), name='solution-detail'),
]
