import React, { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { lessonsAPI, progressAPI } from '../services/api';

const LessonDetail = () => {
  const { id } = useParams();
  const navigate = useNavigate();
  const [lesson, setLesson] = useState(null);
  const [loading, setLoading] = useState(true);
  const [currentQuiz, setCurrentQuiz] = useState(0);
  const [answers, setAnswers] = useState({});
  const [showResults, setShowResults] = useState(false);

  useEffect(() => {
    fetchLesson();
  }, [id]);

  const fetchLesson = async () => {
    try {
      const response = await lessonsAPI.getById(id);
      setLesson(response.data);
    } catch (error) {
      console.error('Error fetching lesson:', error);
    } finally {
      setLoading(false);
    }
  };

  const handleAnswerSelect = (quizId, answer) => {
    setAnswers({
      ...answers,
      [quizId]: answer,
    });
  };

  const calculateScore = () => {
    if (!lesson?.quizzes) return 0;
    
    const correctAnswers = lesson.quizzes.filter(
      quiz => answers[quiz.id] === quiz.correct_answer
    ).length;
    
    return Math.round((correctAnswers / lesson.quizzes.length) * 100);
  };

  const handleCompleteLesson = async () => {
    const score = calculateScore();
    
    try {
      await progressAPI.updateProgress({
        lesson_id: parseInt(id),
        status: 'completed',
        score: score,
        time_spent: 1200, // Mock 20 minutes
      });
      
      setShowResults(true);
    } catch (error) {
      console.error('Error updating progress:', error);
    }
  };

  if (loading) {
    return <div className="text-center py-8">Loading lesson...</div>;
  }

  if (!lesson) {
    return <div className="text-center py-8">Lesson not found.</div>;
  }

  if (showResults) {
    const score = calculateScore();
    return (
      <div className="card max-w-2xl mx-auto text-center">
        <h2 className="text-2xl font-bold mb-4">Lesson Completed!</h2>
        <div className="text-4xl font-bold text-norsk-blue mb-4">{score}%</div>
        <p className="text-gray-600 mb-6">
          Great job! You've completed "{lesson.title}"
        </p>
        <button
          onClick={() => navigate('/dashboard')}
          className="btn-primary"
        >
          Back to Dashboard
        </button>
      </div>
    );
  }

  return (
    <div className="max-w-4xl mx-auto space-y-6">
      <div className="card">
        <div className="flex justify-between items-start mb-4">
          <h1 className="text-2xl font-bold">{lesson.title}</h1>
          <span className="bg-norsk-blue text-white px-3 py-1 rounded">
            {lesson.cefr_level}
          </span>
        </div>
        
        <div className="text-sm text-gray-600 mb-4">
          {lesson.lesson_type} • {lesson.estimated_duration} minutes
        </div>
      </div>

      {/* Lesson Content */}
      <div className="card">
        <h2 className="text-xl font-semibold mb-4">Lesson Content</h2>
        
        {lesson.content_json.introduction && (
          <p className="text-gray-700 mb-4">{lesson.content_json.introduction}</p>
        )}
        
        {lesson.content_json.vocabulary && (
          <div className="mb-6">
            <h3 className="font-semibold mb-3">Vocabulary</h3>
            <div className="grid grid-cols-1 md:grid-cols-2 gap-3">
              {lesson.content_json.vocabulary.map((item, index) => (
                <div key={index} className="border rounded p-3">
                  <div className="font-medium text-norsk-blue">{item.norwegian}</div>
                  <div className="text-sm text-gray-600">{item.english}</div>
                  <div className="text-xs text-gray-500">/{item.pronunciation}/</div>
                </div>
              ))}
            </div>
          </div>
        )}
        
        {lesson.content_json.cultural_note && (
          <div className="bg-blue-50 p-4 rounded-lg">
            <h4 className="font-semibold text-norsk-blue mb-2">Cultural Note</h4>
            <p className="text-sm">{lesson.content_json.cultural_note}</p>
          </div>
        )}
      </div>

      {/* Quizzes */}
      {lesson.quizzes && lesson.quizzes.length > 0 && (
        <div className="card">
          <h2 className="text-xl font-semibold mb-4">Practice Questions</h2>
          
          {lesson.quizzes.map((quiz, index) => (
            <div key={quiz.id} className="mb-6 p-4 border rounded-lg">
              <h3 className="font-medium mb-3">
                Question {index + 1}: {quiz.question_text}
              </h3>
              
              {quiz.question_type === 'multiple_choice' && quiz.options_json && (
                <div className="space-y-2">
                  {quiz.options_json.map((option, optionIndex) => (
                    <label key={optionIndex} className="flex items-center">
                      <input
                        type="radio"
                        name={`quiz_${quiz.id}`}
                        value={option}
                        onChange={() => handleAnswerSelect(quiz.id, option)}
                        className="mr-2"
                      />
                      {option}
                    </label>
                  ))}
                </div>
              )}
            </div>
          ))}
          
          <button
            onClick={handleCompleteLesson}
            className="btn-primary w-full"
            disabled={Object.keys(answers).length < lesson.quizzes.length}
          >
            Complete Lesson
          </button>
        </div>
      )}
    </div>
  );
};

export default LessonDetail;