# NorskLær API Specification

## Base URL
```
Development: http://localhost:8000/api/v1/
Production: https://norsklaer.com/api/v1/
```

## Authentication
- **Type**: JWT (JSON Web Token) Bearer Authentication
- **Header**: `Authorization: Bearer <token>`
- **Token Expiry**: 24 hours
- **Refresh**: Available via `/auth/refresh/` endpoint

## Core Endpoints

### Authentication Endpoints

#### POST /auth/register/
**Purpose**: User account creation
```json
Request:
{
  "email": "user@example.com",
  "password": "securePassword123",
  "first_name": "John",
  "last_name": "Doe",
  "current_cefr_level": "A1",
  "target_cefr_level": "B2"
}

Response (201):
{
  "user_id": 1,
  "email": "user@example.com",
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
  "refresh_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
}
```

#### POST /auth/login/
**Purpose**: User authentication
```json
Request:
{
  "email": "user@example.com",
  "password": "securePassword123"
}

Response (200):
{
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
  "refresh_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
  "user": {
    "id": 1,
    "email": "user@example.com",
    "current_cefr_level": "A1",
    "target_cefr_level": "B2"
  }
}
```

### User Management Endpoints

#### GET /users/profile/
**Purpose**: Retrieve current user profile
**Authentication**: Required
```json
Response (200):
{
  "id": 1,
  "email": "user@example.com",
  "first_name": "John",
  "last_name": "Doe",
  "current_cefr_level": "A1",
  "target_cefr_level": "B2",
  "created_at": "2024-01-15T10:30:00Z"
}
```

#### PUT /users/profile/
**Purpose**: Update user profile
**Authentication**: Required
```json
Request:
{
  "current_cefr_level": "A2",
  "target_cefr_level": "C1"
}

Response (200):
{
  "message": "Profile updated successfully",
  "current_cefr_level": "A2",
  "target_cefr_level": "C1"
}
```

### Lesson Management Endpoints

#### GET /lessons/
**Purpose**: Retrieve available lessons for user's level
**Authentication**: Required
**Query Parameters**: 
- `cefr_level` (optional): Filter by specific level
- `lesson_type` (optional): vocabulary, grammar, listening, speaking
```json
Response (200):
{
  "count": 25,
  "results": [
    {
      "id": 1,
      "title": "Basic Greetings",
      "cefr_level": "A1",
      "lesson_type": "vocabulary",
      "difficulty_score": 2,
      "estimated_duration": 15,
      "user_progress": {
        "status": "completed",
        "score": 85,
        "attempts": 2
      }
    }
  ]
}
```

#### GET /lessons/{id}/
**Purpose**: Retrieve specific lesson content
**Authentication**: Required
```json
Response (200):
{
  "id": 1,
  "title": "Basic Greetings",
  "cefr_level": "A1",
  "lesson_type": "vocabulary",
  "content_json": {
    "introduction": "Learn essential Norwegian greetings",
    "vocabulary": [
      {"norwegian": "Hei", "english": "Hello", "pronunciation": "hi"},
      {"norwegian": "Ha det", "english": "Goodbye", "pronunciation": "ha-de"}
    ]
  },
  "quizzes": [
    {
      "id": 1,
      "question_text": "How do you say 'Hello' in Norwegian?",
      "question_type": "multiple_choice",
      "options_json": ["Hei", "Ha det", "Takk", "Unnskyld"]
    }
  ]
}
```

### Progress Tracking Endpoints

#### GET /progress/
**Purpose**: Retrieve user's learning progress
**Authentication**: Required
```json
Response (200):
{
  "overall_progress": {
    "current_level": "A1",
    "completion_percentage": 65,
    "lessons_completed": 13,
    "total_lessons": 20
  },
  "recent_activity": [
    {
      "lesson_id": 5,
      "lesson_title": "Numbers 1-20",
      "completed_at": "2024-01-15T14:30:00Z",
      "score": 92
    }
  ]
}
```

#### POST /progress/
**Purpose**: Update lesson progress
**Authentication**: Required
```json
Request:
{
  "lesson_id": 1,
  "status": "completed",
  "score": 85,
  "time_spent": 900
}

Response (201):
{
  "message": "Progress updated successfully",
  "lesson_id": 1,
  "status": "completed",
  "score": 85,
  "attempts": 1
}
```

### Speech Recognition Endpoints

#### POST /speech/analyze/
**Purpose**: Process speech input for pronunciation feedback
**Authentication**: Required
**Content-Type**: multipart/form-data
```json
Request:
{
  "audio_file": <binary_audio_data>,
  "quiz_id": 1,
  "expected_text": "Hei, jeg heter John"
}

Response (200):
{
  "transcribed_text": "Hei, jeg heter John",
  "accuracy_score": 88,
  "feedback": {
    "overall": "Good pronunciation",
    "word_analysis": [
      {"word": "Hei", "accuracy": 95, "feedback": "Excellent"},
      {"word": "jeg", "accuracy": 80, "feedback": "Slight improvement needed"},
      {"word": "heter", "accuracy": 90, "feedback": "Very good"},
      {"word": "John", "accuracy": 85, "feedback": "Good effort"}
    ]
  }
}
```

## Error Responses

### Standard Error Format
```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Invalid input data",
    "details": {
      "email": ["This field is required"],
      "password": ["Password must be at least 8 characters"]
    }
  }
}
```

### HTTP Status Codes
- **200**: Success
- **201**: Created
- **400**: Bad Request (validation errors)
- **401**: Unauthorized (invalid/missing token)
- **403**: Forbidden (insufficient permissions)
- **404**: Not Found
- **429**: Too Many Requests (rate limiting)
- **500**: Internal Server Error

## Rate Limiting
- **Authentication endpoints**: 5 requests per minute
- **General API**: 100 requests per minute per user
- **Speech processing**: 10 requests per minute per user

## Data Validation Rules
- **Email**: Valid email format, unique
- **Password**: Minimum 8 characters, alphanumeric
- **CEFR Levels**: Must be A1, A2, B1, B2, C1, or C2
- **Scores**: Integer between 0-100
- **Audio Files**: Maximum 10MB, WAV/MP3 format only