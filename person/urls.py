from django.urls import path

from .views import *

urlpatterns = [
    path('', PersonList.as_view(), name='person_list'),
    path('<int:pk>/', ShowPerson.as_view(), name='show_person'),
]
