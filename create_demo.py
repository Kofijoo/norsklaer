#!/usr/bin/env python
"""
Demo Setup Script for NorskLær Portfolio
Creates demo users and sample progress data
"""
import os
import sys
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'norsklaer_backend.settings')
sys.path.append('backend')
django.setup()

from django.contrib.auth import get_user_model
from norsklaer_backend.apps.lessons.models import Lesson
from norsklaer_backend.apps.progress.models import UserProgress
from django.utils import timezone

User = get_user_model()

def create_demo_data():
    print("Creating demo users and progress data...")
    
    # Create demo user
    demo_user, created = User.objects.get_or_create(
        email='demo@norsklaer.com',
        defaults={
            'username': 'demo_user',
            'first_name': 'Demo',
            'last_name': 'User',
            'current_cefr_level': 'A1',
            'target_cefr_level': 'B2',
        }
    )
    
    if created:
        demo_user.set_password('demo123')
        demo_user.save()
        print(f"✓ Created demo user: {demo_user.email}")
    else:
        print(f"✓ Demo user already exists: {demo_user.email}")
    
    # Create admin user
    admin_user, created = User.objects.get_or_create(
        email='admin@norsklaer.com',
        defaults={
            'username': 'admin',
            'first_name': 'Admin',
            'last_name': 'User',
            'current_cefr_level': 'C2',
            'target_cefr_level': 'C2',
            'is_staff': True,
            'is_superuser': True,
        }
    )
    
    if created:
        admin_user.set_password('admin123')
        admin_user.save()
        print(f"✓ Created admin user: {admin_user.email}")
    else:
        print(f"✓ Admin user already exists: {admin_user.email}")
    
    # Add sample progress for demo user
    lessons = Lesson.objects.all()[:3]  # First 3 lessons
    
    for i, lesson in enumerate(lessons):
        progress, created = UserProgress.objects.get_or_create(
            user=demo_user,
            lesson=lesson,
            defaults={
                'status': 'completed' if i < 2 else 'in_progress',
                'score': 85 + (i * 5) if i < 2 else None,
                'attempts': i + 1,
                'time_spent': 900 + (i * 300),  # 15-30 minutes
                'completed_at': timezone.now() if i < 2 else None,
            }
        )
        
        if created:
            print(f"✓ Added progress for lesson: {lesson.title}")
    
    print("\n" + "="*50)
    print("Demo Setup Complete!")
    print("="*50)
    print("Demo Credentials:")
    print(f"Email: demo@norsklaer.com")
    print(f"Password: demo123")
    print()
    print("Admin Credentials:")
    print(f"Email: admin@norsklaer.com") 
    print(f"Password: admin123")
    print()
    print("Access Points:")
    print("Frontend: http://localhost")
    print("Admin Panel: http://localhost:8000/admin/")
    print("API: http://localhost:8000/api/v1/")

if __name__ == "__main__":
    create_demo_data()