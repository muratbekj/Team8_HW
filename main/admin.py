from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Recipe)
admin.site.register(MealPlan)
admin.site.register(GroceryItem)
admin.site.register(FavoriteRecipe)