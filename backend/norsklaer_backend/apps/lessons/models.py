from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Lesson(models.Model):
    CEFR_LEVELS = [
        ('A1', 'A1'), ('A2', 'A2'), ('B1', 'B1'),
        ('B2', 'B2'), ('C1', 'C1'), ('C2', 'C2'),
    ]
    
    LESSON_TYPES = [
        ('vocabulary', 'Vocabulary'),
        ('grammar', 'Grammar'),
        ('listening', 'Listening'),
        ('speaking', 'Speaking'),
    ]
    
    title = models.CharField(max_length=255)
    cefr_level = models.CharField(max_length=2, choices=CEFR_LEVELS)
    lesson_type = models.CharField(max_length=50, choices=LESSON_TYPES)
    content_json = models.JSONField()
    difficulty_score = models.IntegerField(default=1)
    estimated_duration = models.IntegerField(help_text="Duration in minutes")
    prerequisites = models.JSONField(default=list, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'lessons'
        indexes = [
            models.Index(fields=['cefr_level']),
            models.Index(fields=['lesson_type']),
        ]

class Quiz(models.Model):
    QUESTION_TYPES = [
        ('multiple_choice', 'Multiple Choice'),
        ('fill_blank', 'Fill in the Blank'),
        ('speaking', 'Speaking'),
        ('listening', 'Listening'),
    ]
    
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='quizzes')
    question_text = models.TextField()
    question_type = models.CharField(max_length=20, choices=QUESTION_TYPES)
    correct_answer = models.TextField()
    options_json = models.JSONField(null=True, blank=True)
    audio_file_url = models.URLField(null=True, blank=True)
    difficulty_weight = models.DecimalField(max_digits=3, decimal_places=2, default=1.0)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'quizzes'