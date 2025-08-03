#!/usr/bin/env python
"""
Complete test runner for NorskLær backend
Handles database setup, sample data loading, and API testing
"""
import os
import sys
import subprocess
import time

def run_command(command, description, check_output=False):
    """Run a command and handle errors"""
    print(f"\n{description}...")
    try:
        if check_output:
            result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
            return result.stdout.strip()
        else:
            subprocess.run(command, shell=True, check=True)
        print(f"✓ {description} completed")
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ {description} failed: {e}")
        return False

def check_server_running():
    """Check if Django server is running"""
    try:
        import requests
        response = requests.get("http://127.0.0.1:8000/admin/", timeout=2)
        return True
    except:
        return False

def main():
    print("NorskLær Backend Test Suite")
    print("=" * 50)
    
    # Check if we're in the right directory
    if not os.path.exists("manage.py"):
        print("Error: Please run this script from the backend directory")
        return
    
    # Check if virtual environment is activated
    if not hasattr(sys, 'real_prefix') and not (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
        print("⚠️  Warning: Virtual environment not detected")
        print("Please activate: venv\\Scripts\\activate (Windows) or source venv/bin/activate (Unix)")
    
    # Install requirements
    if not run_command("pip install -r requirements.txt", "Installing dependencies"):
        return
    
    # Run migrations
    if not run_command("python manage.py makemigrations", "Creating migrations"):
        return
    
    if not run_command("python manage.py migrate", "Applying migrations"):
        return
    
    # Load sample data
    if not run_command("python manage.py load_sample_data", "Loading sample Norwegian lesson data"):
        return
    
    # Check if server is already running
    if check_server_running():
        print("✓ Django server is already running")
    else:
        print("\nStarting Django development server...")
        print("Please run in another terminal: python manage.py runserver")
        print("Then press Enter to continue with API tests...")
        input()
    
    # Run API tests
    print("\nRunning API tests...")
    try:
        subprocess.run([sys.executable, "test_api.py"], check=True)
    except subprocess.CalledProcessError:
        print("API tests failed - make sure the server is running")
    
    print("\n" + "=" * 50)
    print("Test suite completed!")
    print("\nNext steps for portfolio demonstration:")
    print("1. Create superuser: python manage.py createsuperuser")
    print("2. Access admin panel: http://127.0.0.1:8000/admin/")
    print("3. Test API endpoints: http://127.0.0.1:8000/api/v1/")
    print("4. Document API responses for portfolio")

if __name__ == "__main__":
    main()