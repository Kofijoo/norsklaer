from django.db import models
from django.contrib.auth import get_user_model
from norsklaer_backend.apps.lessons.models import Lesson

User = get_user_model()

class UserProgress(models.Model):
    STATUS_CHOICES = [
        ('not_started', 'Not Started'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('mastered', 'Mastered'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='progress_set')
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='progress_set')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='not_started')
    score = models.IntegerField(null=True, blank=True)
    attempts = models.IntegerField(default=0)
    time_spent = models.IntegerField(default=0, help_text="Time spent in seconds")
    completed_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'user_progress'
        unique_together = ['user', 'lesson']
        indexes = [
            models.Index(fields=['user']),
            models.Index(fields=['lesson']),
            models.Index(fields=['status']),
        ]