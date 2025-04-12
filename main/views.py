import requests
import os
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, TemplateView, DetailView
from django.db.models import Q
from django.shortcuts import render
from .models import Recipe
from urllib.parse import urlencode
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


class HomeView(ListView):
    model = Recipe  # Assuming you have a Recipe model, but you're fetching from an external API.
    template_name = 'main/home.html'
    context_object_name = 'recipes'  # Context to pass to the template
    api_key_file = 'api_key_file'

    def get_queryset(self):
        # Fetch query parameters from the request
        search_query = self.request.GET.get('q', '')
        cuisine = self.request.GET.get('cuisine', '')
        meal_type = self.request.GET.get('meal_type', '')

        # Fetch API key from environment variable
        API_KEY = open(self.api_key_file, 'r').read()
        if not API_KEY:
            print("API key not found!")

        url = 'https://api.spoonacular.com/recipes/complexSearch'

        params = {
            'apiKey': API_KEY,
            'query': search_query,
            'cuisine': cuisine,
            'type': meal_type,
        }

        full_url = f"{url}?{urlencode(params)}"
        print("Fetching from:", full_url)

        response = requests.get(url, params=params)

        if response.status_code == 200:
            data = response.json()
            print("API response data:", data)
            recipes = data.get('results', [])
        else:
            print("Error fetching recipes:", response.status_code)
            print(response.text)
            recipes = []

        # Return the recipes data as a context
        return recipes
    
class RecipeDetailView(DetailView):
    template_name = 'main/recipe_detail.html'

    def get(self, request, *args, **kwargs):
        recipe_id = kwargs.get('pk')
        api_key = open('api_key_file', 'r').read()

        url = f'https://api.spoonacular.com/recipes/{recipe_id}/information'
        params = {'apiKey': api_key}

        response = requests.get(url, params=params)

        if response.status_code == 200:
            recipe = response.json()
        else:
            recipe = {}

        return render(request, self.template_name, {'recipe': recipe})