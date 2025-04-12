from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

# User Profile View to display user details
class UserProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'main/user_profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user  # Pass the logged-in user to the template
        return context

# Dashboard View
class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'main/dashboard.html'


class HomeView(TemplateView):
    template_name = 'main/home.html'