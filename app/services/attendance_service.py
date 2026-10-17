
class AttendanceService:
    def __init__(self):
        self.attendance_records = []

    def add_record(self, record):
        self.attendance_records.append(record)
        return record

    def get_all_records(self):
        return self.attendance_records

    def get_student_attendance(self, student_id):
        return [
            record for record in self.attendance_records
            if record.student_id == student_id
        ]
