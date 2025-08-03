#!/usr/bin/env python
"""
Development setup script for NorskLær backend
Run this script to set up the development environment
"""
import os
import sys
import subprocess

def run_command(command, description):
    """Run a command and handle errors"""
    print(f"\n{description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✓ {description} completed successfully")
        return result
    except subprocess.CalledProcessError as e:
        print(f"✗ {description} failed: {e}")
        print(f"Error output: {e.stderr}")
        return None

def main():
    print("Setting up NorskLær Backend Development Environment")
    print("=" * 50)
    
    # Check if virtual environment is activated
    if not hasattr(sys, 'real_prefix') and not (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
        print("⚠️  Warning: Virtual environment not detected. Please activate your virtual environment first.")
        print("Run: python -m venv venv && venv\\Scripts\\activate (Windows) or source venv/bin/activate (Unix)")
        return
    
    # Install requirements
    run_command("pip install -r requirements.txt", "Installing Python dependencies")
    
    # Make migrations
    run_command("python manage.py makemigrations", "Creating database migrations")
    
    # Apply migrations
    run_command("python manage.py migrate", "Applying database migrations")
    
    # Create superuser (optional)
    print("\n" + "=" * 50)
    print("Setup completed! Next steps:")
    print("1. Create a superuser: python manage.py createsuperuser")
    print("2. Start the development server: python manage.py runserver")
    print("3. Access admin panel: http://127.0.0.1:8000/admin/")
    print("4. API will be available at: http://127.0.0.1:8000/api/v1/")

if __name__ == "__main__":
    main()