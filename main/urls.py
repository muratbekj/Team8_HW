from django.urls import path, include
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('recipe/<int:pk>/', RecipeDetailView.as_view(), name='recipe_detail'),
    path('save_recipe/<int:pk>/', SaveRecipeView.as_view(), name='save_recipe'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('profile/', UserProfileView.as_view(), name='user_profile'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # others
    path('accounts/', include('accounts.urls'))
]
