from rest_framework import serializers
from .models import UserProgress
from norsklaer_backend.apps.lessons.models import Lesson

class ProgressUpdateSerializer(serializers.ModelSerializer):
    lesson_id = serializers.IntegerField(write_only=True)
    
    class Meta:
        model = UserProgress
        fields = ('lesson_id', 'status', 'score', 'time_spent')
    
    def validate_lesson_id(self, value):
        try:
            lesson = Lesson.objects.get(id=value)
            # Check if user has access to this lesson based on CEFR level
            user = self.context['request'].user
            cefr_order = ['A1', 'A2', 'B1', 'B2', 'C1', 'C2']
            user_level_index = cefr_order.index(user.current_cefr_level)
            lesson_level_index = cefr_order.index(lesson.cefr_level)
            
            if lesson_level_index > user_level_index:
                raise serializers.ValidationError("Lesson not available for your current level")
            return value
        except Lesson.DoesNotExist:
            raise serializers.ValidationError("Lesson does not exist")

class UserProgressSerializer(serializers.ModelSerializer):
    lesson_title = serializers.CharField(source='lesson.title', read_only=True)
    lesson_cefr_level = serializers.CharField(source='lesson.cefr_level', read_only=True)
    
    class Meta:
        model = UserProgress
        fields = ('id', 'lesson_title', 'lesson_cefr_level', 'status', 'score', 
                 'attempts', 'time_spent', 'completed_at', 'updated_at')