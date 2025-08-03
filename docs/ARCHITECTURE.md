# NorskLær System Architecture

## System Overview
NorskLær is a microservices-based Norwegian language learning platform designed for scalability and maintainability.

## Core Components

### 1. Frontend Layer (React.js)
- **Purpose**: User interface and experience
- **Responsibilities**: 
  - CEFR level selection (A1-C2)
  - Lesson delivery and interaction
  - Progress visualization
  - Speech input capture
- **Communication**: REST API calls to backend

### 2. Backend API Layer (Django REST Framework)
- **Purpose**: Business logic and data management
- **Responsibilities**:
  - User authentication and authorization
  - Lesson content management
  - Progress tracking algorithms
  - API endpoint management
- **Database**: PostgreSQL for relational data

### 3. ML/AI Layer (TensorFlow/Whisper)
- **Purpose**: Intelligent features
- **Responsibilities**:
  - Speech recognition and pronunciation feedback
  - Adaptive learning path generation
  - Progress analysis and recommendations
- **Integration**: Microservice architecture with REST endpoints

### 4. Data Layer (PostgreSQL)
- **Purpose**: Persistent data storage
- **Entities**:
  - Users and authentication
  - Lesson content and structure
  - Progress tracking and analytics
  - CEFR proficiency mappings

## Data Flow Architecture

```
User Input → React Frontend → Django API → PostgreSQL Database
                    ↓
            ML Processing → Speech/Adaptive Logic → Updated User State
```

## Scalability Considerations
- **Horizontal Scaling**: Containerized services via Docker
- **Caching**: Redis for session and frequently accessed data
- **CDN**: Static assets served via CloudFront
- **Database**: Read replicas for performance optimization

## Security Architecture
- **Authentication**: JWT token-based system
- **Authorization**: Role-based access control (RBAC)
- **Data Protection**: GDPR compliance for EU users
- **API Security**: Rate limiting and input validation