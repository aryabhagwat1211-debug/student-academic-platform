from flask import Blueprint, jsonify, request
from app.models.student import Student
from app.services.student_service import StudentService

api = Blueprint("api", __name__)
student_service = StudentService()

@api.route("/students", methods=["POST"])
def add_student():
    data = request.get_json()

    student = Student(
        data["student_id"],
        data["name"],
        data["email"],
        data["department"]
    )

    student_service.add_student(student)

    return jsonify(student.to_dict()), 201

@api.route("/students", methods=["GET"])
def get_students():
    students = student_service.get_all_students()
    return jsonify([student.to_dict() for student in students])

@api.route("/students/<student_id>", methods=["GET"])
def get_student(student_id):
    student = student_service.get_student(student_id)

    if student is None:
        return jsonify({"error": "Student not found"}), 404

    return jsonify(student.to_dict())

