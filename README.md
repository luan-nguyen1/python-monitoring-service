# Python Monitoring Microservice

A simple microservice that provides system metrics via REST API.

## Features

- CPU, memory, and disk usage metrics
- Health check endpoint
- Containerized with Docker
- Kubernetes deployment ready

## Local Development

1. Create and activate virtual environment
2. Install dependencies: `pip install -r requirements.txt`
3. Run the application: `python app.py`
4. Access the API at http://localhost:8080

## Docker

Build the image:

docker build -t monitoring-service:latest .


Run the container:
docker run -p 8080:8080 monitoring-service:latest


## Kubernetes Deployment

Apply the manifests:
kubectl apply -f kubernetes/


## API Endpoints

- `/metrics` - Get system metrics
- `/health` - Health check endpoint