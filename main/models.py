from django.db import models
from django.conf import settings

class Recipe(models.Model):
    MEAL_TYPES = [
        ('main-course', 'Main Course'),
        ('side-dish', 'Side Dish'),
        ('dessert', 'Dessert'),
        ('appetizer', 'Appetizer'),
        ('salad', 'Salad'),
        ('bread', 'Bread'),
        ('breakfast', 'Breakfast'),
        ('soup', 'Soup'),
        ('beverage', 'Beverage'),
        ('sauce', 'Sauce'),
    ]
    title = models.CharField(max_length=255)
    cuisine = models.CharField(max_length=100, null=True, blank=True)
    meal_type = models.CharField(max_length=20, choices=MEAL_TYPES, null=True, blank=True)
    description = models.TextField()
    ingredients = models.TextField()
    instructions = models.TextField()
    image_url = models.URLField(blank=True, null=True)
    prep_time = models.IntegerField()
    cook_time = models.IntegerField()
    calories = models.IntegerField()
    protein = models.FloatField(null=True, blank=True)
    carbs = models.FloatField(null=True, blank=True)
    fat = models.FloatField(null=True, blank=True)
    source_url = models.URLField(blank=True, null=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title

class MealPlan(models.Model):
    MEAL_TYPES = [
        ('breakfast', 'Breakfast'),
        ('lunch', 'Lunch'),
        ('dinner', 'Dinner'),
        ('snack', 'Snack'),
    ]
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateField()
    meal_type = models.CharField(max_length=10, choices=MEAL_TYPES)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.meal_type} on {self.date}"

class GroceryItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    unit = models.CharField(max_length=50)
    is_checked = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} - {self.quantity} {self.unit}"

class FavoriteRecipe(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.recipe.title}"
