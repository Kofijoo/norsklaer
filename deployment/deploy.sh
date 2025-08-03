#!/bin/bash

# NorskLær Deployment Script
# Usage: ./deploy.sh [development|production]

set -e

ENVIRONMENT=${1:-development}

echo "Deploying NorskLær in $ENVIRONMENT mode..."

if [ "$ENVIRONMENT" = "production" ]; then
    echo "Production deployment"
    
    # Check if .env file exists
    if [ ! -f .env ]; then
        echo "Error: .env file not found. Copy .env.example and configure it."
        exit 1
    fi
    
    # Build and start production services
    docker-compose -f docker-compose.prod.yml down
    docker-compose -f docker-compose.prod.yml build --no-cache
    docker-compose -f docker-compose.prod.yml up -d
    
    echo "Production deployment completed!"
    echo "Application available at: http://localhost"
    
else
    echo "Development deployment"
    
    # Build and start development services
    docker-compose down
    docker-compose build
    docker-compose up -d
    
    echo "Development deployment completed!"
    echo "Frontend: http://localhost"
    echo "Backend API: http://localhost:8000/api/v1/"
    echo "Admin Panel: http://localhost:8000/admin/"
fi

echo ""
echo "Useful commands:"
echo "  View logs: docker-compose logs -f"
echo "  Stop services: docker-compose down"
echo "  Rebuild: docker-compose build --no-cache"