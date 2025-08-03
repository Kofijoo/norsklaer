-- NorskLær Database Schema
-- PostgreSQL Implementation

-- Users table for authentication and profiles
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    current_cefr_level VARCHAR(2) CHECK (current_cefr_level IN ('A1', 'A2', 'B1', 'B2', 'C1', 'C2')),
    target_cefr_level VARCHAR(2) CHECK (target_cefr_level IN ('A1', 'A2', 'B1', 'B2', 'C1', 'C2')),
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Lessons table for core learning content
CREATE TABLE lessons (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    cefr_level VARCHAR(2) NOT NULL CHECK (cefr_level IN ('A1', 'A2', 'B1', 'B2', 'C1', 'C2')),
    lesson_type VARCHAR(50) NOT NULL CHECK (lesson_type IN ('vocabulary', 'grammar', 'listening', 'speaking')),
    content_json JSONB NOT NULL,
    difficulty_score INTEGER CHECK (difficulty_score BETWEEN 1 AND 10),
    estimated_duration INTEGER NOT NULL, -- minutes
    prerequisites JSONB DEFAULT '[]', -- array of lesson IDs
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- User progress tracking
CREATE TABLE user_progress (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    lesson_id INTEGER REFERENCES lessons(id) ON DELETE CASCADE,
    status VARCHAR(20) NOT NULL CHECK (status IN ('not_started', 'in_progress', 'completed', 'mastered')),
    score INTEGER CHECK (score BETWEEN 0 AND 100),
    attempts INTEGER DEFAULT 0,
    time_spent INTEGER DEFAULT 0, -- seconds
    completed_at TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(user_id, lesson_id)
);

-- Quiz questions for assessments
CREATE TABLE quizzes (
    id SERIAL PRIMARY KEY,
    lesson_id INTEGER REFERENCES lessons(id) ON DELETE CASCADE,
    question_text TEXT NOT NULL,
    question_type VARCHAR(20) NOT NULL CHECK (question_type IN ('multiple_choice', 'fill_blank', 'speaking', 'listening')),
    correct_answer TEXT NOT NULL,
    options_json JSONB, -- for multiple choice options
    audio_file_url VARCHAR(500), -- for listening exercises
    difficulty_weight DECIMAL(3,2) DEFAULT 1.0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Speech recognition attempts
CREATE TABLE speech_attempts (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    quiz_id INTEGER REFERENCES quizzes(id) ON DELETE CASCADE,
    audio_file_path VARCHAR(500) NOT NULL,
    transcribed_text TEXT,
    expected_text TEXT NOT NULL,
    accuracy_score INTEGER CHECK (accuracy_score BETWEEN 0 AND 100),
    feedback_json JSONB, -- detailed pronunciation analysis
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Indexes for performance optimization
CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_lessons_cefr_level ON lessons(cefr_level);
CREATE INDEX idx_user_progress_user_id ON user_progress(user_id);
CREATE INDEX idx_user_progress_lesson_id ON user_progress(lesson_id);
CREATE INDEX idx_quizzes_lesson_id ON quizzes(lesson_id);
CREATE INDEX idx_speech_attempts_user_id ON speech_attempts(user_id);

-- Triggers for updated_at timestamps
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ language 'plpgsql';

CREATE TRIGGER update_users_updated_at BEFORE UPDATE ON users FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();
CREATE TRIGGER update_lessons_updated_at BEFORE UPDATE ON lessons FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();
CREATE TRIGGER update_user_progress_updated_at BEFORE UPDATE ON user_progress FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();