# NorskLær - Norwegian Language Learning Platform

[![Live Demo](https://img.shields.io/badge/Live-Demo-blue)](http://localhost)
[![Docker](https://img.shields.io/badge/Docker-Ready-green)](https://docker.com)
[![License](https://img.shields.io/badge/License-Portfolio-orange)](LICENSE)

> **Portfolio Project**: A full-stack language learning platform demonstrating modern web development practices and educational technology expertise.

## 🎯 Project Overview

NorskLær is a comprehensive Norwegian language learning platform designed for Norway's 150,000+ immigrant population requiring language certification. Built as a portfolio demonstration of full-stack development capabilities, it showcases professional-grade architecture, user experience design, and educational domain expertise.

### 🏆 Key Achievements
- **Zero-Budget Development**: Built entirely with free tools and services
- **Professional Architecture**: Microservices design with Docker containerization
- **Educational Expertise**: CEFR-compliant curriculum and progress tracking
- **Modern Tech Stack**: React.js, Django REST Framework, PostgreSQL
- **Production Ready**: Complete CI/CD pipeline and deployment configuration

## Technology Stack

### Backend
- **Python 3.11+** with **Django 4.2** and **Django REST Framework**
- **PostgreSQL 15** for relational data storage with JSONB support
- **JWT Authentication** for stateless user sessions
- **Docker** containerization for consistent deployment

### Frontend
- **React.js 18+** with modern hooks and context API
- **Tailwind CSS** for utility-first responsive design
- **Axios** for API communication with interceptors

### AI/ML Components
- **TensorFlow Lite** for edge-optimized model deployment
- **OpenAI Whisper** for multilingual speech recognition
- **Custom adaptive learning algorithms** for personalized curriculum

### Infrastructure
- **AWS Free Tier**: EC2, S3, CloudFront CDN
- **GitHub Actions** for CI/CD pipeline
- **Docker Compose** for local development orchestration

## Key Features

### 🎯 Adaptive Learning Engine
- Personalized curriculum based on user performance
- CEFR level progression tracking (A1 → C2)
- Prerequisite-based lesson unlocking system

### 🗣️ Speech Recognition & Pronunciation
- Real-time Norwegian pronunciation feedback
- Word-level accuracy scoring
- Cultural pronunciation variations support

### 📊 Progress Analytics
- Comprehensive learning analytics dashboard
- Time-spent tracking and engagement metrics
- Performance trends and improvement suggestions

### 🏛️ Cultural Context Integration
- Norwegian workplace communication scenarios
- Citizenship test preparation content
- Regional dialect awareness

## Architecture Overview

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   React.js      │    │   Django REST   │    │   PostgreSQL    │
│   Frontend      │◄──►│   API Backend   │◄──►│   Database      │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │
         │                       │                       │
         ▼                       ▼                       ▼
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   CDN Assets    │    │   ML/AI Models  │    │   File Storage  │
│   (CloudFront)  │    │   (TensorFlow)  │    │   (AWS S3)      │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

## Project Structure

```
norsklær/
├── docs/                    # Architecture and API documentation
│   ├── ARCHITECTURE.md      # System design overview
│   ├── TECH_STACK.md       # Technology choices and justifications
│   ├── API_SPECIFICATION.md # Complete REST API documentation
│   └── ERD.md              # Database relationship diagrams
├── backend/                 # Django REST API
│   └── api_endpoints.py    # URL structure and routing
├── frontend/               # React.js application
├── ml-models/             # AI/ML components and models
├── database/              # Database schemas and migrations
│   ├── models.md          # Entity documentation
│   └── schema.sql         # PostgreSQL implementation
├── deployment/            # Docker and deployment configurations
└── README.md             # This file
```

## Quick Start

### Prerequisites
- Python 3.11+
- Node.js 18+
- PostgreSQL 15+
- Docker & Docker Compose

### Development Setup
```bash
# Clone repository
git clone https://github.com/yourusername/norsklaer.git
cd norsklaer

# Backend setup
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

# Frontend setup (new terminal)
cd frontend
npm install
npm start

# Database setup
createdb norsklaer_dev
psql norsklaer_dev < database/schema.sql
```

### Docker Development
```bash
docker-compose up --build
```

## API Documentation

The platform provides a comprehensive REST API with JWT authentication:

- **Authentication**: `/api/v1/auth/` - Registration, login, token refresh
- **User Management**: `/api/v1/users/` - Profile management and preferences
- **Lessons**: `/api/v1/lessons/` - CEFR-based lesson content and structure
- **Progress**: `/api/v1/progress/` - Learning analytics and completion tracking
- **Speech**: `/api/v1/speech/` - Pronunciation analysis and feedback

Full API specification available in [`docs/API_SPECIFICATION.md`](docs/API_SPECIFICATION.md)

## Database Design

The platform uses a normalized PostgreSQL schema optimized for educational content:

- **Users**: Authentication and CEFR level tracking
- **Lessons**: Structured content with prerequisite relationships
- **Progress**: Individual learning analytics and completion status
- **Quizzes**: Assessment questions with multiple formats
- **Speech Attempts**: Pronunciation tracking and feedback storage

Complete database documentation in [`database/models.md`](database/models.md)

## Development Approach

### Zero-Budget Constraints
This project demonstrates professional development practices within free-tier limitations:
- AWS Free Tier for cloud infrastructure
- Open-source tools and frameworks
- Optimized for portfolio demonstration rather than production scale

### Technical Achievements
- **Microservices Architecture**: Scalable component separation
- **RESTful API Design**: Industry-standard endpoint structure
- **Database Optimization**: Strategic indexing and JSONB usage
- **Security Implementation**: JWT authentication and input validation
- **Performance Considerations**: Caching strategies and query optimization

## Target Market Analysis

### Primary Users
- **Norwegian Language Learners**: Immigrants requiring certification
- **Employment Seekers**: Workplace communication skills
- **Citizenship Candidates**: Official language requirements

### Market Opportunity
- 150,000+ immigrant population in Norway
- Mandatory language certification for employment/citizenship
- Limited personalized learning solutions for Norwegian

## Future Enhancements

### Phase 2 Features
- Real-time conversation practice with AI tutors
- Gamification elements and achievement systems
- Integration with Norwegian official certification bodies
- Mobile application for iOS and Android

### Scaling Considerations
- Kubernetes orchestration for container management
- Redis caching layer for improved performance
- CDN optimization for global content delivery
- Advanced ML models for more sophisticated adaptation

## Contributing

This project serves as a portfolio demonstration of edtech development capabilities. For collaboration or technical discussions, please reach out via [your contact information].

## License

This project is developed for portfolio purposes. All rights reserved.

---

**Technical Contact**: Joshua Agyekum -  joshuaagyekum21@gmail.com  - https://github.com/Kofijoo
**Portfolio**: https://kofijoo.github.io/edtech.github.io/  
**LinkedIn**: https://www.linkedin.com/in/joshua-agyekum