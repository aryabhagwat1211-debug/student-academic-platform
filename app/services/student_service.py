from app.models.student import Student

class StudentService:
    def __init__(self):
        self.students = {}

    def add_student(self, student):
        self.students[student.student_id] = student

    def get_student(self, student_id):
        return self.students.get(student_id)

    def get_all_students(self):
        return list(self.students.values())

    def delete_student(self, student_id):
        return self.students.pop(student_id, None)

