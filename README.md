# Student Academic Management Platform

## Overview

A Flask-based Student Academic Management Platform developed as a DevOps project. The application provides student record APIs, automated tests, containerization with Docker, and orchestration with Kubernetes using Minikube.

## Technology Stack

- Python 3.11
- Flask
- Pytest
- Git and GitHub
- Docker
- Kubernetes
- Minikube

## Features

- Student registration
- Student lookup and listing
- Health monitoring API
- Automated unit and API testing
- Docker containerization
- Kubernetes deployment with three replicas
- Readiness and liveness probes
- CPU and memory resource limits

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/health` | Check application health |
| GET | `/api/students` | List students |
| GET | `/api/students/<student_id>` | Retrieve a student by ID |
| POST | `/api/students` | Register a student |

## Project Structure

```text
student-academic-platform/
├── app/
│   ├── models/
│   ├── routes/
│   └── services/
├── database/
├── tests/
├── k8s/
│   ├── deployment.yaml
│   └── service.yaml
├── Dockerfile
├── requirements.txt
├── run.py
└── README.md
```

## Run Locally

Install dependencies:

```bash
pip install -r requirements.txt
```

Start the application:

```bash
python run.py
```

The application listens on port 5000.

Health check: `http://localhost:5000/api/health`

## Testing

Run the test suite:

```bash
pytest -v
```

## Docker

Build the Docker image:

```bash
docker build -t student-academic-platform:latest .
```

Run the container:

```bash
docker run --rm -p 5000:5000 student-academic-platform:latest
```

Test the health endpoint at `http://localhost:5000/api/health`.

## Kubernetes with Minikube

Start Minikube:

```bash
minikube start --driver=docker
```

Build the image and make it available inside Minikube:

```bash
docker build -t student-academic-platform:latest .
minikube image load student-academic-platform:latest
```

Apply the Kubernetes manifests:

```bash
kubectl apply -f k8s/
```

Check the deployment and service:

```bash
kubectl get nodes
kubectl get pods
kubectl get deployments
kubectl get services
```

The deployment is configured for three replicas. The service exposes container port 5000 through NodePort 30081.

Access the application through port forwarding:

```bash
kubectl port-forward service/student-academic-service 8081:5000
```

Keep the port-forward terminal open and visit `http://127.0.0.1:8081/`.

Test the health endpoint at `http://127.0.0.1:8081/api/health`.

## Repository

GitHub: https://github.com/aryabhagwat1211-debug/student-academic-platform
