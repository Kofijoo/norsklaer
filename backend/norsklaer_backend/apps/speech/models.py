from django.db import models
from django.contrib.auth import get_user_model
from norsklaer_backend.apps.lessons.models import Quiz

User = get_user_model()

class SpeechAttempt(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='speech_attempts')
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='speech_attempts')
    audio_file_path = models.CharField(max_length=500)
    transcribed_text = models.TextField(null=True, blank=True)
    expected_text = models.TextField()
    accuracy_score = models.IntegerField(null=True, blank=True)
    feedback_json = models.JSONField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'speech_attempts'
        indexes = [
            models.Index(fields=['user']),
            models.Index(fields=['quiz']),
            models.Index(fields=['created_at']),
        ]