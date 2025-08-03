# Django URL Configuration for NorskLær API
# This file demonstrates the planned URL structure for the REST API

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# API versioning through URL namespace
app_name = 'api_v1'

# ViewSet router for standard CRUD operations
router = DefaultRouter()
router.register(r'lessons', views.LessonViewSet, basename='lesson')
router.register(r'progress', views.UserProgressViewSet, basename='progress')
router.register(r'quizzes', views.QuizViewSet, basename='quiz')

urlpatterns = [
    # Authentication endpoints
    path('auth/register/', views.UserRegistrationView.as_view(), name='register'),
    path('auth/login/', views.UserLoginView.as_view(), name='login'),
    path('auth/refresh/', views.TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/logout/', views.UserLogoutView.as_view(), name='logout'),
    
    # User management endpoints
    path('users/profile/', views.UserProfileView.as_view(), name='user_profile'),
    path('users/profile/update/', views.UserProfileUpdateView.as_view(), name='profile_update'),
    
    # Speech recognition endpoints
    path('speech/analyze/', views.SpeechAnalysisView.as_view(), name='speech_analysis'),
    path('speech/attempts/', views.SpeechAttemptListView.as_view(), name='speech_attempts'),
    
    # Adaptive learning endpoints
    path('recommendations/', views.LessonRecommendationView.as_view(), name='recommendations'),
    path('analytics/progress/', views.ProgressAnalyticsView.as_view(), name='progress_analytics'),
    
    # Include router URLs for ViewSets
    path('', include(router.urls)),
]

# URL Pattern Examples:
# GET  /api/v1/auth/login/           - User authentication
# POST /api/v1/auth/register/       - User registration
# GET  /api/v1/users/profile/       - Get user profile
# PUT  /api/v1/users/profile/update/ - Update user profile
# GET  /api/v1/lessons/             - List lessons for user's level
# GET  /api/v1/lessons/1/           - Get specific lesson content
# POST /api/v1/progress/            - Update lesson progress
# GET  /api/v1/progress/            - Get user's progress summary
# POST /api/v1/speech/analyze/      - Process speech input
# GET  /api/v1/recommendations/     - Get adaptive learning suggestions

# ViewSet automatically generates:
# GET    /api/v1/lessons/           - list()
# POST   /api/v1/lessons/           - create()
# GET    /api/v1/lessons/{id}/      - retrieve()
# PUT    /api/v1/lessons/{id}/      - update()
# PATCH  /api/v1/lessons/{id}/      - partial_update()
# DELETE /api/v1/lessons/{id}/      - destroy()

# Authentication Strategy:
# - JWT tokens for stateless authentication
# - Token-based authorization for all protected endpoints
# - Refresh token mechanism for extended sessions
# - Rate limiting implemented at middleware level

# Permission Classes:
# - IsAuthenticated: For all user-specific endpoints
# - IsOwner: For user profile and progress endpoints
# - IsAdminUser: For lesson management (future admin panel)

# Serializer Strategy:
# - Separate serializers for input/output data transformation
# - Nested serializers for complex relationships (lesson + progress)
# - Custom validation for CEFR levels and business rules