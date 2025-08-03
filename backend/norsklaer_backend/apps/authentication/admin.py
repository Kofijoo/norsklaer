from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'current_cefr_level', 'is_active')
    list_filter = ('current_cefr_level', 'target_cefr_level', 'is_active')
    search_fields = ('email', 'first_name', 'last_name')
    
    fieldsets = UserAdmin.fieldsets + (
        ('CEFR Levels', {'fields': ('current_cefr_level', 'target_cefr_level')}),
    )