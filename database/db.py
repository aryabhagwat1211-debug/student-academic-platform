class StudentDatabase:
    def __init__(self):
        self.students = {}

    def save_student(self, student):
        self.students[student.student_id] = student

    def find_student(self, student_id):
        return self.students.get(student_id)

    def get_all_students(self):
        return list(self.students.values())

    def delete_student(self, student_id):
        return self.students.pop(student_id, None)

