#!/usr/bin/env python
"""
API Testing Script for NorskLær Backend
Tests core functionality without requiring frontend
"""
import requests
import json

BASE_URL = "http://127.0.0.1:8000/api/v1"

def test_user_registration():
    """Test user registration endpoint"""
    print("\n=== Testing User Registration ===")
    
    user_data = {
        "email": "test@norsklaer.com",
        "username": "testuser",
        "first_name": "Test",
        "last_name": "User",
        "current_cefr_level": "A1",
        "target_cefr_level": "B2",
        "password": "testpass123",
        "password_confirm": "testpass123"
    }
    
    try:
        response = requests.post(f"{BASE_URL}/auth/register/", json=user_data)
        print(f"Status: {response.status_code}")
        print(f"Response: {response.json()}")
        return response.status_code == 201
    except Exception as e:
        print(f"Error: {e}")
        return False

def test_user_login():
    """Test user login and get JWT token"""
    print("\n=== Testing User Login ===")
    
    login_data = {
        "email": "test@norsklaer.com",
        "password": "testpass123"
    }
    
    try:
        response = requests.post(f"{BASE_URL}/auth/login/", json=login_data)
        print(f"Status: {response.status_code}")
        data = response.json()
        print(f"Response: {data}")
        
        if response.status_code == 200:
            return data.get('access')
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

def test_lessons_api(token):
    """Test lessons endpoint with authentication"""
    print("\n=== Testing Lessons API ===")
    
    headers = {"Authorization": f"Bearer {token}"}
    
    try:
        response = requests.get(f"{BASE_URL}/lessons/", headers=headers)
        print(f"Status: {response.status_code}")
        data = response.json()
        print(f"Found {len(data.get('results', []))} lessons")
        
        for lesson in data.get('results', [])[:3]:  # Show first 3 lessons
            print(f"- {lesson['title']} ({lesson['cefr_level']}) - {lesson['lesson_type']}")
        
        return response.status_code == 200
    except Exception as e:
        print(f"Error: {e}")
        return False

def test_lesson_detail(token):
    """Test individual lesson detail"""
    print("\n=== Testing Lesson Detail ===")
    
    headers = {"Authorization": f"Bearer {token}"}
    
    try:
        response = requests.get(f"{BASE_URL}/lessons/1/", headers=headers)
        print(f"Status: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            print(f"Lesson: {data['title']}")
            print(f"Content: {len(data['content_json'])} sections")
            print(f"Quizzes: {len(data['quizzes'])} questions")
        
        return response.status_code == 200
    except Exception as e:
        print(f"Error: {e}")
        return False

def test_progress_update(token):
    """Test progress update functionality"""
    print("\n=== Testing Progress Update ===")
    
    headers = {"Authorization": f"Bearer {token}"}
    progress_data = {
        "lesson_id": 1,
        "status": "completed",
        "score": 85,
        "time_spent": 900  # 15 minutes in seconds
    }
    
    try:
        response = requests.post(f"{BASE_URL}/progress/update/", json=progress_data, headers=headers)
        print(f"Status: {response.status_code}")
        print(f"Response: {response.json()}")
        return response.status_code == 201
    except Exception as e:
        print(f"Error: {e}")
        return False

def test_progress_list(token):
    """Test progress listing with analytics"""
    print("\n=== Testing Progress Analytics ===")
    
    headers = {"Authorization": f"Bearer {token}"}
    
    try:
        response = requests.get(f"{BASE_URL}/progress/", headers=headers)
        print(f"Status: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            overall = data.get('overall_progress', {})
            print(f"Current Level: {overall.get('current_level')}")
            print(f"Completion: {overall.get('completion_percentage')}%")
            print(f"Completed Lessons: {overall.get('lessons_completed')}/{overall.get('total_lessons')}")
        
        return response.status_code == 200
    except Exception as e:
        print(f"Error: {e}")
        return False

def main():
    """Run all API tests"""
    print("NorskLær API Testing Suite")
    print("=" * 40)
    
    # Test registration
    if not test_user_registration():
        print("Registration failed - user might already exist, continuing...")
    
    # Test login and get token
    token = test_user_login()
    if not token:
        print("Login failed - cannot continue with authenticated tests")
        return
    
    # Test authenticated endpoints
    test_lessons_api(token)
    test_lesson_detail(token)
    test_progress_update(token)
    test_progress_list(token)
    
    print("\n" + "=" * 40)
    print("API testing completed!")
    print("Next steps:")
    print("1. Check Django admin: http://127.0.0.1:8000/admin/")
    print("2. View API documentation: http://127.0.0.1:8000/api/v1/")
    print("3. Test with different CEFR levels and lesson types")

if __name__ == "__main__":
    main()