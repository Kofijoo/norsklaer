#!/usr/bin/env python
"""
Database Fix Script for NorskLær
Recreates database with proper Django migrations
"""
import subprocess
import sys

def run_command(command, description):
    print(f"\n{description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✓ {description} completed")
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ {description} failed: {e}")
        print(f"Error output: {e.stderr}")
        return False

def main():
    print("Fixing NorskLær Database Schema")
    print("=" * 40)
    
    # Stop containers
    print("Stopping containers...")
    subprocess.run("docker-compose down", shell=True)
    
    # Remove database volume to start fresh
    print("Removing database volume...")
    subprocess.run("docker volume rm norsklr_postgres_data", shell=True)
    
    # Rebuild and start
    print("Starting fresh deployment...")
    if not run_command("docker-compose up --build -d", "Building and starting containers"):
        return
    
    # Wait for services to be ready
    print("Waiting for services to initialize...")
    import time
    time.sleep(30)
    
    # Create demo data
    print("Creating demo users...")
    run_command("python create_demo.py", "Setting up demo data")
    
    print("\n" + "=" * 40)
    print("Database Fix Complete!")
    print("=" * 40)
    print("Access Points:")
    print("Frontend: http://localhost")
    print("Admin Panel: http://localhost:8000/admin/")
    print()
    print("Demo Credentials:")
    print("Email: demo@norsklaer.com")
    print("Password: demo123")
    print()
    print("Admin Credentials:")
    print("Email: admin@norsklaer.com")
    print("Password: admin123")

if __name__ == "__main__":
    main()