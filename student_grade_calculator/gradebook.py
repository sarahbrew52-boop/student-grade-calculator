"""Class-wide gradebook: many students, many courses."""

from __future__ import annotations

from .student import Student


class GradeBook:
    """Top-level container for a whole class of students."""

    def __init__(self):
        self.students: dict[str, Student] = {}

    def add_student(self, student_id: str, name: str) -> Student:
        """Register a student (idempotent) and return their Student object."""
        if student_id not in self.students:
            self.students[student_id] = Student(student_id, name)
        return self.students[student_id]

    def add_score(self, student_id: str, course_name: str, assessment: str,
                  score: float, weight: float | None = None) -> None:
        if student_id not in self.students:
            raise KeyError(f"Unknown student_id {student_id!r}; call add_student() first")
        self.students[student_id].add_score(course_name, assessment, score, weight)

    def class_average(self, course_name: str) -> float:
        """Average weighted score for a given course, across all enrolled students."""
        scores = [
            s.
