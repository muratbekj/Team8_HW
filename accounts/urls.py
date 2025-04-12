from django.urls import path
from .views import *

urlpatterns = [
    path('register/', UserCreateView.as_view(), name='register'),
    path('', UserListView.as_view(), name='user_list'),
    path('<int:pk>/', UserDetailView.as_view(), name='user_detail'),
    path('<int:pk>/edit/', UserUpdateView.as_view(), name='user_edit'),
    path('<int:pk>/delete/', UserDeleteView.as_view(), name='user_delete'),
]
