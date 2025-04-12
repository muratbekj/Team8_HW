from django.urls import path
from .views import UserCreateView, UserDetailView, UserUpdateView, UserDeleteView

urlpatterns = [
    path('signup/', UserCreateView.as_view(), name='signup'),
    path('profile/', UserDetailView.as_view(), name='user_profile'),
    path('edit/', UserUpdateView.as_view(), name='user_edit'),
    path('delete/', UserDeleteView.as_view(), name='user_delete'),
]
