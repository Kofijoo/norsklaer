from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone
from .models import UserProgress
from .serializers import ProgressUpdateSerializer, UserProgressSerializer
from norsklaer_backend.apps.lessons.models import Lesson

class ProgressUpdateView(generics.CreateAPIView):
    serializer_class = ProgressUpdateSerializer
    permission_classes = [IsAuthenticated]
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        lesson_id = serializer.validated_data['lesson_id']
        lesson = Lesson.objects.get(id=lesson_id)
        
        # Get or create progress record
        progress, created = UserProgress.objects.get_or_create(
            user=request.user,
            lesson=lesson,
            defaults={'status': 'not_started'}
        )
        
        # Update progress
        progress.status = serializer.validated_data['status']
        progress.score = serializer.validated_data.get('score', progress.score)
        progress.time_spent += serializer.validated_data.get('time_spent', 0)
        progress.attempts += 1
        
        if progress.status == 'completed':
            progress.completed_at = timezone.now()
        
        progress.save()
        
        return Response({
            'message': 'Progress updated successfully',
            'lesson_id': lesson_id,
            'status': progress.status,
            'score': progress.score,
            'attempts': progress.attempts
        }, status=status.HTTP_201_CREATED)

class UserProgressListView(generics.ListAPIView):
    serializer_class = UserProgressSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return UserProgress.objects.filter(user=self.request.user).select_related('lesson')
    
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        
        # Calculate overall progress statistics
        total_lessons = queryset.count()
        completed_lessons = queryset.filter(status='completed').count()
        completion_percentage = (completed_lessons / total_lessons * 100) if total_lessons > 0 else 0
        
        return Response({
            'overall_progress': {
                'current_level': request.user.current_cefr_level,
                'completion_percentage': round(completion_percentage, 1),
                'lessons_completed': completed_lessons,
                'total_lessons': total_lessons
            },
            'progress_details': serializer.data
        })