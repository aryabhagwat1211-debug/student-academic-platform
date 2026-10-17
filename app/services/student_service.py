
class StudentService:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)
        return student

    def get_all_students(self):
        return self.students

    def find_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None

    def get_student(self, student_id):
        return self.find_student(student_id)
