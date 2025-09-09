import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { lessonsAPI, progressAPI } from '../services/api';
import { useAuth } from '../context/AuthContext';
import LoadingSpinner from '../components/LoadingSpinner';
import ErrorMessage from '../components/ErrorMessage';
import ProgressChart from '../components/ProgressChart';

const Dashboard = () => {
  const [lessons, setLessons] = useState([]);
  const [progress, setProgress] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const { user } = useAuth();

  useEffect(() => {
    fetchData();
  }, []);

  const fetchData = async () => {
    try {
      setError(null);
      const [lessonsResponse, progressResponse] = await Promise.all([
        lessonsAPI.getAll(),
        progressAPI.getProgress(),
      ]);
      
      setLessons(lessonsResponse.data.results || []);
      setProgress(progressResponse.data);
    } catch (error) {
      setError('Failed to load dashboard data. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  if (loading) {
    return <LoadingSpinner text="Loading your learning dashboard..." />;
  }

  if (error) {
    return <ErrorMessage message={error} onRetry={fetchData} />;
  }

  return (
    <div className="space-y-6">
      <div className="flex flex-col sm:flex-row sm:justify-between sm:items-center gap-4">
        <h1 className="text-2xl sm:text-3xl font-bold text-gray-900">
          Welcome back, {user?.first_name}!
        </h1>
        <div className="text-sm text-gray-600">
          Current Level: <span className="font-semibold text-norsk-blue">{user?.current_cefr_level}</span>
        </div>
      </div>

      {/* Progress Overview */}
      <ProgressChart progress={progress} />

      {/* Available Lessons */}
      <div className="card">
        <h2 className="text-xl font-semibold mb-4">Available Lessons</h2>
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
          {lessons.map((lesson) => (
            <div key={lesson.id} className="border rounded-lg p-4 hover:shadow-md transition-shadow">
              <div className="flex justify-between items-start mb-2">
                <h3 className="font-semibold text-gray-900">{lesson.title}</h3>
                <span className="text-xs bg-norsk-blue text-white px-2 py-1 rounded">
                  {lesson.cefr_level}
                </span>
              </div>
              
              <div className="text-sm text-gray-600 mb-2">
                Type: {lesson.lesson_type} • {lesson.estimated_duration} min
              </div>
              
              {lesson.user_progress && (
                <div className="text-sm mb-3">
                  Status: <span className="font-medium text-green-600">
                    {lesson.user_progress.status.replace('_', ' ')}
                  </span>
                  {lesson.user_progress.score && (
                    <span className="ml-2">Score: {lesson.user_progress.score}%</span>
                  )}
                </div>
              )}
              
              <Link
                to={`/lesson/${lesson.id}`}
                className="btn-primary text-sm w-full text-center block"
              >
                {lesson.user_progress?.status === 'completed' ? 'Review' : 'Start Lesson'}
              </Link>
            </div>
          ))}
        </div>
        
        {lessons.length === 0 && (
          <div className="text-center text-gray-600 py-8">
            No lessons available for your current level.
          </div>
        )}
      </div>
    </div>
  );
};

export default Dashboard;