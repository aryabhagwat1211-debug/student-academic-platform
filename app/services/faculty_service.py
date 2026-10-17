
class FacultyService:
    def __init__(self):
        self.faculty_members = []

    def add_faculty(self, faculty):
        self.faculty_members.append(faculty)
        return faculty

    def get_all_faculty(self):
        return self.faculty_members

    def find_faculty(self, faculty_id):
        for faculty in self.faculty_members:
            if faculty.faculty_id == faculty_id:
                return faculty
        return None
