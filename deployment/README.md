# NorskLær Deployment Guide

## Quick Start

### Development Deployment
```bash
# Clone repository
git clone <repository-url>
cd norsklaer

# Start all services
docker-compose up --build

# Access application
# Frontend: http://localhost
# Backend API: http://localhost:8000/api/v1/
# Admin Panel: http://localhost:8000/admin/
```

### Production Deployment
```bash
# Configure environment
cp .env.example .env
# Edit .env with production values

# Deploy
docker-compose -f docker-compose.prod.yml up --build -d
```

## Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Nginx         │    │   Django        │    │   PostgreSQL    │
│   (Frontend)    │◄──►│   (Backend)     │◄──►│   (Database)    │
│   Port 80       │    │   Port 8000     │    │   Port 5432     │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

## Services

### Database (PostgreSQL)
- **Image**: postgres:15-alpine
- **Port**: 5432
- **Volume**: postgres_data
- **Health Check**: Included

### Backend (Django)
- **Build**: ./backend/Dockerfile
- **Port**: 8000
- **Features**: REST API, JWT Auth, Admin Panel
- **Auto-migration**: Runs on startup

### Frontend (React + Nginx)
- **Build**: ./frontend/Dockerfile
- **Port**: 80
- **Features**: SPA with API proxy
- **Static Optimization**: Enabled

## Environment Variables

### Required for Production
```env
DATABASE_NAME=norsklaer_prod
DATABASE_USER=norsklaer_user
DATABASE_PASSWORD=secure_password
SECRET_KEY=production-secret-key
ALLOWED_HOSTS=yourdomain.com
API_BASE_URL=https://yourdomain.com/api/v1
```

## Monitoring and Maintenance

### View Logs
```bash
# All services
docker-compose logs -f

# Specific service
docker-compose logs -f backend
```

### Database Backup
```bash
docker-compose exec db pg_dump -U postgres norsklaer_dev > backup.sql
```

### Update Application
```bash
git pull
docker-compose build --no-cache
docker-compose up -d
```

## Scaling Considerations

### Horizontal Scaling
- Use Docker Swarm or Kubernetes
- Load balancer for multiple frontend instances
- Database read replicas

### Performance Optimization
- Redis for caching
- CDN for static assets
- Database connection pooling

## Security

### Production Checklist
- [ ] Change default passwords
- [ ] Use HTTPS (SSL/TLS)
- [ ] Configure firewall
- [ ] Regular security updates
- [ ] Database backups
- [ ] Monitor logs

## Troubleshooting

### Common Issues

**Database Connection Failed**
```bash
docker-compose logs db
docker-compose restart db
```

**Frontend Build Failed**
```bash
docker-compose build --no-cache frontend
```

**Backend Migration Issues**
```bash
docker-compose exec backend python manage.py migrate
```

## Free Hosting Options

### Development/Portfolio
- **Render.com**: Free tier with limitations
- **Railway**: $5 monthly credit
- **Heroku**: Limited free tier

### Database
- **Supabase**: Free PostgreSQL (500MB)
- **PlanetScale**: Free MySQL tier
- **Railway**: Included with hosting

### Static Assets
- **Netlify**: Free frontend hosting
- **Vercel**: Free React deployment
- **GitHub Pages**: Static site hosting