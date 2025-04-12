from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    DIET_CHOICES = [
        ('vegan', 'Vegan'),
        ('keto', 'Keto'),
        ('gluten_free', 'Gluten-Free'),
    ]

    diet_preference = models.CharField(
        max_length=20,
        choices=DIET_CHOICES,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.username
