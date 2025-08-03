from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/auth/', include('norsklaer_backend.apps.authentication.urls')),
    path('api/v1/lessons/', include('norsklaer_backend.apps.lessons.urls')),
    path('api/v1/progress/', include('norsklaer_backend.apps.progress.urls')),
    path('api/v1/speech/', include('norsklaer_backend.apps.speech.urls')),
]