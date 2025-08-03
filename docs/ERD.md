# Entity Relationship Diagram (ERD)

## Visual Database Structure

```
┌─────────────────┐       ┌─────────────────┐       ┌─────────────────┐
│     USERS       │       │    LESSONS      │       │   USER_PROGRESS │
├─────────────────┤       ├─────────────────┤       ├─────────────────┤
│ id (PK)         │       │ id (PK)         │       │ id (PK)         │
│ email (UNIQUE)  │       │ title           │       │ user_id (FK)    │
│ password_hash   │       │ cefr_level      │       │ lesson_id (FK)  │
│ first_name      │       │ lesson_type     │       │ status          │
│ last_name       │       │ content_json    │       │ score           │
│ current_cefr    │       │ difficulty_score│       │ attempts        │
│ target_cefr     │       │ estimated_duration      │ time_spent      │
│ is_active       │       │ prerequisites   │       │ completed_at    │
│ created_at      │       │ created_at      │       │ created_at      │
│ updated_at      │       │ updated_at      │       │ updated_at      │
└─────────────────┘       └─────────────────┘       └─────────────────┘
         │                         │                         │
         │                         │                         │
         │                         └─────────────────────────┘
         │                                   │
         │                                   │
         │                 ┌─────────────────┐
         │                 │    QUIZZES      │
         │                 ├─────────────────┤
         │                 │ id (PK)         │
         │                 │ lesson_id (FK)  │
         │                 │ question_text   │
         │                 │ question_type   │
         │                 │ correct_answer  │
         │                 │ options_json    │
         │                 │ audio_file_url  │
         │                 │ difficulty_weight│
         │                 │ created_at      │
         │                 └─────────────────┘
         │                         │
         │                         │
         │                         │
         │                 ┌─────────────────┐
         └─────────────────│ SPEECH_ATTEMPTS │
                           ├─────────────────┤
                           │ id (PK)         │
                           │ user_id (FK)    │
                           │ quiz_id (FK)    │
                           │ audio_file_path │
                           │ transcribed_text│
                           │ expected_text   │
                           │ accuracy_score  │
                           │ feedback_json   │
                           │ created_at      │
                           └─────────────────┘
```

## Relationship Types

### Primary Relationships
- **Users ↔ UserProgress**: One-to-Many (1:N)
  - One user can have progress on multiple lessons
  - Each progress record belongs to exactly one user

- **Lessons ↔ UserProgress**: One-to-Many (1:N)
  - One lesson can be attempted by multiple users
  - Each progress record tracks exactly one lesson

- **Lessons ↔ Quizzes**: One-to-Many (1:N)
  - One lesson can have multiple quiz questions
  - Each quiz question belongs to exactly one lesson

- **Users ↔ SpeechAttempts**: One-to-Many (1:N)
  - One user can make multiple speech attempts
  - Each speech attempt belongs to exactly one user

- **Quizzes ↔ SpeechAttempts**: One-to-Many (1:N)
  - One quiz question can have multiple speech attempts
  - Each speech attempt responds to exactly one quiz question

## Data Integrity Rules

### Constraints
- **CEFR Levels**: Enforced enum values (A1, A2, B1, B2, C1, C2)
- **Lesson Types**: Enforced enum values (vocabulary, grammar, listening, speaking)
- **Progress Status**: Enforced enum values (not_started, in_progress, completed, mastered)
- **Score Ranges**: 0-100 validation on all score fields
- **Unique Constraints**: User-Lesson combination in UserProgress table

### Cascading Rules
- **User Deletion**: Cascades to UserProgress and SpeechAttempts
- **Lesson Deletion**: Cascades to UserProgress and Quizzes
- **Quiz Deletion**: Cascades to SpeechAttempts

## Performance Considerations
- **Indexes**: Created on foreign keys and frequently queried fields
- **JSONB Fields**: Used for flexible content storage with query optimization
- **Timestamps**: Automatic triggers for audit trail maintenance