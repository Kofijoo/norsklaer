# Development Environment Setup Guide

## System Requirements

### Minimum Specifications
- **OS**: Windows 10/11, macOS 10.15+, or Ubuntu 20.04+
- **RAM**: 8GB minimum, 16GB recommended
- **Storage**: 5GB free space for development environment
- **Network**: Stable internet connection for package downloads

### Required Software Versions
- **Python**: 3.11 or higher
- **Node.js**: 18.0 or higher
- **PostgreSQL**: 15.0 or higher
- **Git**: 2.30 or higher
- **Docker**: 20.10 or higher (optional but recommended)

## Step-by-Step Setup

### 1. Repository Setup
```bash
# Clone the repository
git clone https://github.com/yourusername/norsklaer.git
cd norsklaer

# Verify project structure
ls -la
# Should show: backend/, frontend/, docs/, database/, ml-models/, deployment/
```

### 2. Database Setup (PostgreSQL)

#### Windows Installation
```bash
# Download PostgreSQL from https://www.postgresql.org/download/windows/
# During installation, remember the superuser password

# Create development database
createdb -U postgres norsklaer_dev

# Import schema
psql -U postgres -d norsklaer_dev -f database/schema.sql
```

#### macOS Installation
```bash
# Using Homebrew
brew install postgresql@15
brew services start postgresql@15

# Create database
createdb norsklaer_dev
psql norsklaer_dev < database/schema.sql
```

#### Ubuntu Installation
```bash
# Install PostgreSQL
sudo apt update
sudo apt install postgresql postgresql-contrib

# Create database
sudo -u postgres createdb norsklaer_dev
sudo -u postgres psql norsklaer_dev < database/schema.sql
```

### 3. Backend Setup (Django)

```bash
# Navigate to backend directory
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install django==4.2.7
pip install djangorestframework==3.14.0
pip install psycopg2-binary==2.9.7
pip install djangorestframework-simplejwt==5.3.0
pip install django-cors-headers==4.3.1
pip install python-decouple==3.8

# Create requirements.txt
pip freeze > requirements.txt

# Django project initialization
django-admin startproject norsklaer_backend .
cd norsklaer_backend
python manage.py startapp authentication
python manage.py startapp lessons
python manage.py startapp progress
python manage.py startapp speech

# Database migrations
python manage.py makemigrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run development server
python manage.py runserver
# Server should start at http://127.0.0.1:8000/
```

### 4. Frontend Setup (React.js)

```bash
# Open new terminal, navigate to frontend directory
cd frontend

# Create React application
npx create-react-app norsklaer-frontend
cd norsklaer-frontend

# Install additional dependencies
npm install axios react-router-dom @tailwindcss/forms
npm install -D tailwindcss postcss autoprefixer

# Initialize Tailwind CSS
npx tailwindcss init -p

# Start development server
npm start
# Application should open at http://localhost:3000/
```

### 5. Environment Configuration

#### Backend Environment Variables
Create `backend/.env` file:
```env
DEBUG=True
SECRET_KEY=your-secret-key-here
DATABASE_NAME=norsklaer_dev
DATABASE_USER=postgres
DATABASE_PASSWORD=your-postgres-password
DATABASE_HOST=localhost
DATABASE_PORT=5432
ALLOWED_HOSTS=localhost,127.0.0.1
CORS_ALLOWED_ORIGINS=http://localhost:3000
```

#### Frontend Environment Variables
Create `frontend/.env` file:
```env
REACT_APP_API_BASE_URL=http://127.0.0.1:8000/api/v1
REACT_APP_ENVIRONMENT=development
```

### 6. Docker Setup (Optional)

#### Create Docker Configuration
Create `docker-compose.yml` in project root:
```yaml
version: '3.8'

services:
  db:
    image: postgres:15
    environment:
      POSTGRES_DB: norsklaer_dev
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: postgres
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data
      - ./database/schema.sql:/docker-entrypoint-initdb.d/schema.sql

  backend:
    build: ./backend
    ports:
      - "8000:8000"
    depends_on:
      - db
    environment:
      - DATABASE_HOST=db
    volumes:
      - ./backend:/app

  frontend:
    build: ./frontend
    ports:
      - "3000:3000"
    volumes:
      - ./frontend:/app
      - /app/node_modules

volumes:
  postgres_data:
```

#### Run with Docker
```bash
# Build and start all services
docker-compose up --build

# Run in background
docker-compose up -d

# Stop services
docker-compose down
```

## Development Workflow

### 1. Daily Development Routine
```bash
# Start backend (Terminal 1)
cd backend
source venv/bin/activate  # Windows: venv\Scripts\activate
python manage.py runserver

# Start frontend (Terminal 2)
cd frontend/norsklaer-frontend
npm start

# Start database (if not using Docker)
# Windows: Start PostgreSQL service
# macOS: brew services start postgresql@15
# Ubuntu: sudo systemctl start postgresql
```

### 2. Code Quality Tools

#### Backend Linting
```bash
# Install development tools
pip install flake8 black isort

# Format code
black .
isort .

# Check code quality
flake8 .
```

#### Frontend Linting
```bash
# Install ESLint and Prettier
npm install -D eslint prettier eslint-config-prettier

# Format code
npx prettier --write src/

# Check code quality
npx eslint src/
```

### 3. Testing Setup

#### Backend Testing
```bash
# Run Django tests
python manage.py test

# Install testing tools
pip install pytest pytest-django coverage

# Run tests with coverage
coverage run -m pytest
coverage report
```

#### Frontend Testing
```bash
# Run React tests
npm test

# Install additional testing tools
npm install -D @testing-library/jest-dom @testing-library/user-event

# Run tests with coverage
npm test -- --coverage
```

## Troubleshooting

### Common Issues

#### Database Connection Errors
```bash
# Check PostgreSQL status
# Windows: Check Services app
# macOS: brew services list | grep postgresql
# Ubuntu: sudo systemctl status postgresql

# Reset database
dropdb norsklaer_dev
createdb norsklaer_dev
psql norsklaer_dev < database/schema.sql
```

#### Python Virtual Environment Issues
```bash
# Remove and recreate virtual environment
rm -rf venv
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

#### Node.js Dependency Issues
```bash
# Clear npm cache and reinstall
rm -rf node_modules package-lock.json
npm cache clean --force
npm install
```

### Performance Optimization

#### Database Query Optimization
```python
# Use select_related for foreign key relationships
lessons = Lesson.objects.select_related('user').all()

# Use prefetch_related for many-to-many relationships
users = User.objects.prefetch_related('progress_set').all()
```

#### Frontend Bundle Optimization
```bash
# Analyze bundle size
npm install -D webpack-bundle-analyzer
npm run build
npx webpack-bundle-analyzer build/static/js/*.js
```

## Development Best Practices

### Git Workflow
```bash
# Create feature branch
git checkout -b feature/lesson-management

# Commit with descriptive messages
git commit -m "feat: add lesson CRUD endpoints with CEFR filtering"

# Push and create pull request
git push origin feature/lesson-management
```

### Code Organization
- **Backend**: Follow Django app structure with models, views, serializers
- **Frontend**: Use component-based architecture with hooks
- **Database**: Maintain migrations and seed data scripts
- **Documentation**: Update API docs with any endpoint changes

### Security Considerations
- Never commit environment variables or secrets
- Use HTTPS in production configurations
- Implement proper input validation and sanitization
- Regular dependency updates for security patches