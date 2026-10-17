class Enrollment:
    def __init__(self, enrollment_id, student_id, course_id, semester):
        self.enrollment_id = enrollment_id
        self.student_id = student_id
        self.course_id = course_id
        self.semester = semester

    def to_dict(self):
        return {
            "enrollment_id": self.enrollment_id,
            "student_id": self.student_id,
            "course_id": self.course_id,
            "semester": self.semester
        }