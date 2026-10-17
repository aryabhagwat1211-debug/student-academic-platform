class AcademicService:

    GRADE_POINTS = {
        "A+": 10,
        "A": 9,
        "B+": 8,
        "B": 7,
        "C": 6,
        "D": 5,
        "F": 0
    }

    def calculate_gpa(self, grades):
        if not grades:
            return 0.0

        total_points = 0
        total_courses = 0

        for grade in grades:
            if grade not in self.GRADE_POINTS:
                raise ValueError("Invalid grade")

            total_points += self.GRADE_POINTS[grade]
            total_courses += 1

        return round(total_points / total_courses, 2)