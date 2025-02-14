#!/bin/bash
set -ex

# Install Docker
sudo apt-get update -y
sudo apt-get install -y docker.io
sudo chown $USER /var/run/docker.sock

# Enable & Start Docker Service
sudo systemctl enable docker
sudo systemctl start docker

# Initialize Docker Swarm
docker swarm init

# Create Secrets
echo "YmI5MThhYWUyYmM2NDUwNzg2YmZiYmQ4MzcyOWExMjY=" | docker secret create SPOTIPY_CLIENT_ID -
echo "ZThjOTJiMGJlZGM0NGVlZjlkYTk3MTVhMzdmMmI3M2E=" | docker secret create SPOTIPY_CLIENT_SECRET -

# Create docker-compose.yml file
cat <<EOF2 > /home/ubuntu/docker-compose.yml
version: "3.7"
services:
  flask-app:
    image: trendz:latest
    ports:
      - "8000:5000"
    secrets:
      - SPOTIPY_CLIENT_ID
      - SPOTIPY_CLIENT_SECRET

secrets:
  SPOTIPY_CLIENT_ID:
    external: true
  SPOTIPY_CLIENT_SECRET:
    external: true
EOF2

# Deploy Flask App with Docker Swarm
docker stack deploy -c /home/ubuntu/docker-compose.yml my_flask_stack
