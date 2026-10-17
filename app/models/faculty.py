class Faculty:
    def __init__(self, faculty_id, name, email, department):
        self.faculty_id = faculty_id
        self.name = name
        self.email = email
        self.department = department

    def to_dict(self):
        return {
            "faculty_id": self.faculty_id,
            "name": self.name,
            "email": self.email,
            "department": self.department
        }