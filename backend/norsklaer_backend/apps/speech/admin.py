from django.contrib import admin
from .models import SpeechAttempt

@admin.register(SpeechAttempt)
class SpeechAttemptAdmin(admin.ModelAdmin):
    list_display = ('user', 'quiz', 'accuracy_score', 'created_at')
    list_filter = ('quiz__question_type', 'accuracy_score')
    search_fields = ('user__email', 'transcribed_text', 'expected_text')