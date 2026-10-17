
from app.services.student_service import StudentService
from app.services.course_service import CourseService
from app.services.faculty_service import FacultyService
from app.services.attendance_service import AttendanceService


def test_student_service():
    service = StudentService()
    assert service.get_all_students() == []


def test_course_service():
    service = CourseService()
    assert service.get_all_courses() == []


def test_faculty_service():
    service = FacultyService()
    assert service.get_all_faculty() == []


def test_attendance_service():
    service = AttendanceService()
    assert service.get_all_records() == []
