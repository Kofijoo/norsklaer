from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    CEFR_LEVELS = [
        ('A1', 'A1 - Beginner'),
        ('A2', 'A2 - Elementary'),
        ('B1', 'B1 - Intermediate'),
        ('B2', 'B2 - Upper Intermediate'),
        ('C1', 'C1 - Advanced'),
        ('C2', 'C2 - Proficient'),
    ]
    
    email = models.EmailField(unique=True)
    current_cefr_level = models.CharField(max_length=2, choices=CEFR_LEVELS, default='A1')
    target_cefr_level = models.CharField(max_length=2, choices=CEFR_LEVELS, default='B2')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
    
    class Meta:
        db_table = 'users'