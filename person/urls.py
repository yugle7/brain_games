from django.urls import path

from .views import *

urlpatterns = [
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),

    path('', PersonList.as_view(), name='person-list'),
    path('<int:pk>/', PersonDetail.as_view(), name='person-detail'),

]
