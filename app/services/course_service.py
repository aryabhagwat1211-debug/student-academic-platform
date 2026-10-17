
class CourseService:
    def __init__(self):
        self.courses = []

    def add_course(self, course):
        self.courses.append(course)
        return course

    def get_all_courses(self):
        return self.courses

    def find_course(self, course_id):
        for course in self.courses:
            if course.course_id == course_id:
                return course
        return None
