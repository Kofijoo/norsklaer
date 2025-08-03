from django.urls import path
from .views import ProgressUpdateView, UserProgressListView

urlpatterns = [
    path('', UserProgressListView.as_view(), name='progress_list'),
    path('update/', ProgressUpdateView.as_view(), name='progress_update'),
]