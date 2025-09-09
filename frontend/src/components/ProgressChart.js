import React from 'react';

const ProgressChart = ({ progress }) => {
  if (!progress?.overall_progress) return null;

  const { completion_percentage, lessons_completed, total_lessons } = progress.overall_progress;
  
  const circumference = 2 * Math.PI * 45;
  const strokeDasharray = circumference;
  const strokeDashoffset = circumference - (completion_percentage / 100) * circumference;

  return (
    <div className="card">
      <h2 className="text-xl font-semibold mb-6">Learning Progress</h2>
      
      <div className="flex items-center justify-center mb-6">
        <div className="relative w-32 h-32">
          <svg className="w-32 h-32 transform -rotate-90" viewBox="0 0 100 100">
            <circle
              cx="50"
              cy="50"
              r="45"
              stroke="#e5e7eb"
              strokeWidth="8"
              fill="none"
            />
            <circle
              cx="50"
              cy="50"
              r="45"
              stroke="#003f7f"
              strokeWidth="8"
              fill="none"
              strokeLinecap="round"
              strokeDasharray={strokeDasharray}
              strokeDashoffset={strokeDashoffset}
              className="transition-all duration-1000 ease-out"
            />
          </svg>
          <div className="absolute inset-0 flex items-center justify-center">
            <div className="text-center">
              <div className="text-2xl font-bold text-norsk-blue">
                {completion_percentage}%
              </div>
              <div className="text-xs text-gray-600">Complete</div>
            </div>
          </div>
        </div>
      </div>

      <div className="grid grid-cols-2 gap-4 text-center">
        <div>
          <div className="text-2xl font-bold text-green-600">{lessons_completed}</div>
          <div className="text-sm text-gray-600">Completed</div>
        </div>
        <div>
          <div className="text-2xl font-bold text-gray-700">{total_lessons}</div>
          <div className="text-sm text-gray-600">Total Lessons</div>
        </div>
      </div>

      {progress.progress_details && progress.progress_details.length > 0 && (
        <div className="mt-6">
          <h3 className="font-semibold mb-3">Recent Activity</h3>
          <div className="space-y-2">
            {progress.progress_details.slice(0, 3).map((item, index) => (
              <div key={index} className="flex justify-between items-center text-sm">
                <span className="text-gray-700">{item.lesson_title}</span>
                <span className={`px-2 py-1 rounded text-xs ${
                  item.status === 'completed' 
                    ? 'bg-green-100 text-green-800' 
                    : 'bg-yellow-100 text-yellow-800'
                }`}>
                  {item.status.replace('_', ' ')}
                </span>
              </div>
            ))}
          </div>
        </div>
      )}
    </div>
  );
};

export default ProgressChart;