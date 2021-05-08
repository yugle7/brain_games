from django.urls import path

from .views import *

urlpatterns = [
    path('', ShowSolution.as_view(), name='solution_list'),
    path('<int:id>/', ShowSolution.as_view(), name='solution_show'),
]
