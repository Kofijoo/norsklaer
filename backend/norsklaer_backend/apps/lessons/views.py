from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from .models import Lesson
from .serializers import LessonSerializer, LessonListSerializer

class LessonListView(generics.ListAPIView):
    serializer_class = LessonListSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['cefr_level', 'lesson_type']
    ordering_fields = ['difficulty_score', 'created_at']
    ordering = ['difficulty_score']
    
    def get_queryset(self):
        user = self.request.user
        # Filter lessons based on user's current CEFR level and below
        cefr_order = ['A1', 'A2', 'B1', 'B2', 'C1', 'C2']
        user_level_index = cefr_order.index(user.current_cefr_level)
        available_levels = cefr_order[:user_level_index + 1]
        
        return Lesson.objects.filter(cefr_level__in=available_levels)

class LessonDetailView(generics.RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        cefr_order = ['A1', 'A2', 'B1', 'B2', 'C1', 'C2']
        user_level_index = cefr_order.index(user.current_cefr_level)
        available_levels = cefr_order[:user_level_index + 1]
        
        return Lesson.objects.filter(cefr_level__in=available_levels).prefetch_related('quizzes')