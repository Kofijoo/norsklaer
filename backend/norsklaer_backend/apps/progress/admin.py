from django.contrib import admin
from .models import UserProgress

@admin.register(UserProgress)
class UserProgressAdmin(admin.ModelAdmin):
    list_display = ('user', 'lesson', 'status', 'score', 'attempts', 'completed_at')
    list_filter = ('status', 'lesson__cefr_level', 'lesson__lesson_type')
    search_fields = ('user__email', 'lesson__title')