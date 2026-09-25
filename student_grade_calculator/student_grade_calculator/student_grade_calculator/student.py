
"""Student model: a student enrolled in multiple courses."""

from __future__ import annotations

from .course import Course


class Student:
    """Represents one student and all the courses they're taking."""

    def __init__(self, student_id: str, name: str):
        self.student_id = student_id
        self.name = name
        self.courses: dict[str, Course] = {}

    def enroll(self, course_name: str) -> Course:
        """Add a course for this student (idempotent) and return it."""
        if course_name not in self.courses:
            self.courses[course_name] = Course(course_name)
        return self.courses[course_name]

    def add_score(self, course_name: str, assessment: str, score: float, weight: float | None = None) -> None:
        course = self.enroll(course_name)
        course.add_score(assessment, score, weight)

    def gpa(self) -> float:
        """Overall GPA: mean of this student's per-course GPA points."""
        if not self.courses:
            return 0.0
        return sum(c.gpa() for c in self.courses.values()) / len(self.courses)

    def transcript(self) -> dict:
        """A summary dict of every course, its average, and letter grade."""
        return {
            "student_id": self.student_id,
            "name": self.name,
            "gpa": round(self.gpa(), 2),
            "courses": {
                name: {
                    "average": round(c.weighted_average(), 2),
                    "letter_grade": c.letter_grade(),
                }
                for name, c in self.courses.items()
            },
        }

    def __repr__(self) -> str:
        return f"Student(id={self.student_id!r}, name={self.name!r}, gpa={self.gpa():.2f})"
