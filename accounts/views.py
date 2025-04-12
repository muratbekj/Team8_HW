from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from .models import User
from .forms import CustomUserCreationForm, CustomUserChangeForm

# User creation view
class UserCreateView(CreateView):
    model = User
    form_class = CustomUserCreationForm
    template_name = 'accounts/register.html'

    def get_success_url(self):
        return reverse_lazy('login')  # Redirect to login after user creation

# User profile detail view
class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'accounts/user_detail.html'
    context_object_name = 'user_obj'

    def get_object(self):
        return self.request.user  # Always return the logged-in user's details

# User update view
class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = CustomUserChangeForm
    template_name = 'accounts/user_edit.html'
    success_url = reverse_lazy('user_profile')  # Redirect to profile after update

    def get_object(self):
        return self.request.user

# User delete view
class UserDeleteView(LoginRequiredMixin, DeleteView):
    model = User
    template_name = 'accounts/user_confirm_delete.html'
    success_url = reverse_lazy('login')  # Redirect to login page after delete

    def get_object(self):
        return self.request.user
