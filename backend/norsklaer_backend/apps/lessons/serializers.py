from rest_framework import serializers
from .models import Lesson, Quiz
from norsklaer_backend.apps.progress.models import UserProgress

class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ('id', 'question_text', 'question_type', 'correct_answer', 
                 'options_json', 'audio_file_url', 'difficulty_weight')

class LessonSerializer(serializers.ModelSerializer):
    quizzes = QuizSerializer(many=True, read_only=True)
    user_progress = serializers.SerializerMethodField()
    
    class Meta:
        model = Lesson
        fields = ('id', 'title', 'cefr_level', 'lesson_type', 'content_json',
                 'difficulty_score', 'estimated_duration', 'prerequisites', 
                 'quizzes', 'user_progress')
    
    def get_user_progress(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            try:
                progress = UserProgress.objects.get(user=request.user, lesson=obj)
                return {
                    'status': progress.status,
                    'score': progress.score,
                    'attempts': progress.attempts,
                    'completed_at': progress.completed_at
                }
            except UserProgress.DoesNotExist:
                return {'status': 'not_started', 'score': None, 'attempts': 0}
        return None

class LessonListSerializer(serializers.ModelSerializer):
    user_progress = serializers.SerializerMethodField()
    
    class Meta:
        model = Lesson
        fields = ('id', 'title', 'cefr_level', 'lesson_type', 'difficulty_score',
                 'estimated_duration', 'user_progress')
    
    def get_user_progress(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            try:
                progress = UserProgress.objects.get(user=request.user, lesson=obj)
                return {
                    'status': progress.status,
                    'score': progress.score,
                    'attempts': progress.attempts
                }
            except UserProgress.DoesNotExist:
                return {'status': 'not_started', 'score': None, 'attempts': 0}
        return None