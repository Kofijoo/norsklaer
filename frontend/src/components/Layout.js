import React from 'react';
import { useAuth } from '../context/AuthContext';

const Layout = ({ children }) => {
  const { user, logout } = useAuth();

  return (
    <div className="min-h-screen bg-norsk-light">
      <nav className="bg-norsk-blue text-white shadow-lg">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between h-16">
            <div className="flex items-center">
              <h1 className="text-xl font-bold">NorskLær</h1>
            </div>
            
            {user && (
              <div className="flex items-center space-x-4">
                <span className="text-sm">
                  {user.first_name} ({user.current_cefr_level})
                </span>
                <button
                  onClick={logout}
                  className="text-sm hover:text-gray-300"
                >
                  Logout
                </button>
              </div>
            )}
          </div>
        </div>
      </nav>
      
      <main className="max-w-7xl mx-auto py-6 px-4 sm:px-6 lg:px-8">
        {children}
      </main>
    </div>
  );
};

export default Layout;