
from app.models.grade import Grade
from app.models.course import Course
from app.models.faculty import Faculty
from app.models.attendance import Attendance


def test_grade_to_dict():
    grade = Grade("STU001", "CSE101", "A")
    assert grade.to_dict()["grade"] == "A"


def test_course_to_dict():
    course = Course("CSE101", "Python Programming", 4)
    assert course.to_dict()["course_id"] == "CSE101"


def test_faculty_to_dict():
    faculty = Faculty(
        "FAC001", "Rahul Sharma",
        "rahul@example.com", "Computer Science"
    )
    assert faculty.to_dict()["email"] == "rahul@example.com"


def test_attendance_percentage():
    attendance = Attendance("STU001", "CSE101", 40, 35)
    assert attendance.attendance_percentage() == 87.5
