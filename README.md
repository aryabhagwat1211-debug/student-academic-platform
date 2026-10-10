# Enterprise Student Record and Academic Management Platform

## Overview

A Flask-based student academic management platform developed as a DevOps project.

## Technology Stack

- Python
- Flask
- Pytest
- Git and GitHub
- Jenkins
- Docker
- Kubernetes
- Minikube

## Features

- Student registration
- Student lookup
- Student listing
- Health monitoring API
- Automated testing

## API Endpoints

GET /api/health
GET /api/students
GET /api/students/<student_id>
POST /api/students

## Running the Application

Activate the virtual environment and run:

python run.py

The application runs on port 5000.

## Testing

Run:

pytest -v

## Project Structure

app/
database/
tests/
k8s/
Dockerfile
Jenkinsfile
requirements.txt
README.md

