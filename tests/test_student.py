from app.models.student import Student

def test_student_creation():
    student = Student(
        "STU001",
        "Arya Bhagwat",
        "arya@example.com",
        "CSE-AIML"
    )

    assert student.student_id == "STU001"
    assert student.name == "Arya Bhagwat"
    assert student.email == "arya@example.com"
    assert student.department == "CSE-AIML"

def test_student_to_dict():
    student = Student(
        "STU002",
        "Test Student",
        "test@example.com",
        "CSE"
    )

    data = student.to_dict()

    assert data["student_id"] == "STU002"
    assert data["name"] == "Test Student"
    assert data["email"] == "test@example.com"
    assert data["department"] == "CSE"

