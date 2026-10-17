
class Attendance:
    def __init__(self, student_id, course_id, total_classes, attended_classes):
        self.student_id = student_id
        self.course_id = course_id
        self.total_classes = total_classes
        self.attended_classes = attended_classes

    def attendance_percentage(self):
        if self.total_classes == 0:
            return 0
        return round((self.attended_classes / self.total_classes) * 100, 2)

    def to_dict(self):
        return {
            "student_id": self.student_id,
            "course_id": self.course_id,
            "total_classes": self.total_classes,
            "attended_classes": self.attended_classes,
            "attendance_percentage": self.attendance_percentage()
        }
