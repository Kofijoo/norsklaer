from django.contrib import admin
from .models import Lesson, Quiz

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'cefr_level', 'lesson_type', 'difficulty_score', 'estimated_duration')
    list_filter = ('cefr_level', 'lesson_type', 'difficulty_score')
    search_fields = ('title',)

@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ('lesson', 'question_type', 'difficulty_weight')
    list_filter = ('question_type', 'lesson__cefr_level')
    search_fields = ('question_text', 'lesson__title')