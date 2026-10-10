import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client

def test_health_endpoint(client):
    response = client.get("/api/health")

    assert response.status_code == 200
    assert response.get_json()["status"] == "healthy"

def test_add_student(client):
    response = client.post(
        "/api/students",
        json={
            "student_id": "STU001",
            "name": "Test Student",
            "email": "test@example.com",
            "department": "CSE-AIML"
        }
    )

    assert response.status_code == 201
    assert response.get_json()["student_id"] == "STU001"

def test_get_student(client):
    client.post(
        "/api/students",
        json={
            "student_id": "STU002",
            "name": "Another Student",
            "email": "another@example.com",
            "department": "CSE"
        }
    )

    response = client.get("/api/students/STU002")

    assert response.status_code == 200
    assert response.get_json()["name"] == "Another Student"

def test_student_not_found(client):
    response = client.get("/api/students/UNKNOWN")

    assert response.status_code == 404

