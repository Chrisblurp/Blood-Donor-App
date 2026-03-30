#!/bin/bash
set -e

echo "🔨 Building Docker images..."

# Build development images
docker compose build

# Build production images
docker compose -f docker-compose.prod.yml build

echo "✅ Build complete!"
echo ""
echo "To run development: docker compose up"
echo "To run production:  docker compose -f docker-compose.prod.yml up -d"
