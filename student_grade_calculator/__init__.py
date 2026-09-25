"""
student_grade_calculator
=========================

A small, dependency-free Python library for computing student grades
across multiple students and multiple courses.

Typical usage:

    from student_grade_calculator import Student, Course, GradeBook

    gb = GradeBook()
    gb.add_student("S001", "Ama Mensah")
    gb.add_score("S001", "Math101", "Midterm", 78, weight=0.4)
    gb.add_score("S001", "Math101", "Final", 85, weight=0.6)

    print(gb.student_report("S001"))
    print(gb.class_average("Math101"))
"""

from .grading import letter_grade, gpa_point, GRADE_SCALE
from .course import Course
from .student import Student
from .gradebook import GradeBook

__all__ = [
    "letter_grade",
    "gpa_point",
    "GRADE_SCALE",
    "Course",
    "Student",
    "GradeBook",
]

__version__ = "0.1.0"
