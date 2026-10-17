
from database.db import StudentDatabase
from app.models.student import Student


def test_save_and_find_student():
    db = StudentDatabase()
    student = Student(
        "STU001", "Arya Bhagwat",
        "arya@example.com", "AIML"
    )
    db.save_student(student)
    assert db.find_student("STU001") is student


def test_get_all_students():
    db = StudentDatabase()
    student = Student(
        "STU001", "Arya Bhagwat",
        "arya@example.com", "AIML"
    )
    db.save_student(student)
    assert len(db.get_all_students()) == 1


def test_delete_student():
    db = StudentDatabase()
    student = Student(
        "STU001", "Arya Bhagwat",
        "arya@example.com", "AIML"
    )
    db.save_student(student)
    db.delete_student("STU001")
    assert db.find_student("STU001") is None
