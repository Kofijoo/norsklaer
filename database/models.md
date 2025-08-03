# Database Models Documentation

## Core Entities

### User
- **Purpose**: Authentication and profile management
- **Fields**:
  - `id` (Primary Key): Unique identifier
  - `email` (Unique): Authentication credential
  - `password_hash`: Encrypted password storage
  - `first_name`, `last_name`: Personal identification
  - `current_cefr_level`: A1, A2, B1, B2, C1, C2
  - `target_cefr_level`: Learning goal
  - `created_at`, `updated_at`: Audit timestamps
  - `is_active`: Account status

### Lesson
- **Purpose**: Core learning content structure
- **Fields**:
  - `id` (Primary Key): Unique identifier
  - `title`: Lesson name
  - `cefr_level`: Target proficiency level
  - `lesson_type`: vocabulary, grammar, listening, speaking
  - `content_json`: Flexible lesson data (questions, audio, text)
  - `difficulty_score`: 1-10 adaptive learning metric
  - `estimated_duration`: Minutes to complete
  - `prerequisites`: JSON array of required lesson IDs
  - `created_at`, `updated_at`: Content versioning

### UserProgress
- **Purpose**: Individual learning tracking
- **Fields**:
  - `id` (Primary Key): Unique identifier
  - `user_id` (Foreign Key): Links to User
  - `lesson_id` (Foreign Key): Links to Lesson
  - `status`: not_started, in_progress, completed, mastered
  - `score`: 0-100 performance metric
  - `attempts`: Number of completion tries
  - `time_spent`: Seconds engaged with content
  - `completed_at`: Timestamp of completion
  - `created_at`, `updated_at`: Progress tracking

### Quiz
- **Purpose**: Assessment and knowledge validation
- **Fields**:
  - `id` (Primary Key): Unique identifier
  - `lesson_id` (Foreign Key): Associated lesson
  - `question_text`: The actual question
  - `question_type`: multiple_choice, fill_blank, speaking, listening
  - `correct_answer`: Expected response
  - `options_json`: Multiple choice options array
  - `audio_file_url`: For listening exercises
  - `difficulty_weight`: Impact on adaptive algorithm

### SpeechAttempt
- **Purpose**: Speech recognition and pronunciation tracking
- **Fields**:
  - `id` (Primary Key): Unique identifier
  - `user_id` (Foreign Key): Links to User
  - `quiz_id` (Foreign Key): Associated quiz question
  - `audio_file_path`: Recorded speech file location
  - `transcribed_text`: Speech-to-text result
  - `expected_text`: Target pronunciation
  - `accuracy_score`: 0-100 pronunciation accuracy
  - `feedback_json`: Detailed pronunciation analysis
  - `created_at`: Recording timestamp

## Relationships

### One-to-Many
- User → UserProgress (one user has many progress records)
- User → SpeechAttempt (one user has many speech attempts)
- Lesson → UserProgress (one lesson tracked by many users)
- Lesson → Quiz (one lesson has many quiz questions)
- Quiz → SpeechAttempt (one quiz question has many speech attempts)

### Business Rules
- Users can only access lessons at or below their current CEFR level
- Lessons must be completed in prerequisite order
- Speech attempts are retained for progress analysis
- Quiz scores influence adaptive learning path recommendations