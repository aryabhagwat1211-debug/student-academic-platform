class Student:
    def __init__(self, student_id, name, email, department):
        self.student_id = student_id
        self.name = name
        self.email = email
        self.department = department

    def to_dict(self):
        return {
            "student_id": self.student_id,
            "name": self.name,
            "email": self.email,
            "department": self.department
        }
