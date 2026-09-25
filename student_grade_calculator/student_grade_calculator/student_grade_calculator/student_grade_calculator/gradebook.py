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
            s.courses[course_name].weighted_average()
            for s in self.students.values()
            if course_name in s.courses
        ]
        if not scores:
            return 0.0
        return sum(scores) / len(scores)

    def top_student(self, course_name: str) -> Student | None:
        """Return the Student with the highest weighted average in a course."""
        candidates = [s for s in self.students.values() if course_name in s.courses]
        if not candidates:
            return None
        return max(candidates, key=lambda s: s.courses[course_name].weighted_average())

    def student_report(self, student_id: str) -> dict:
        return self.students[student_id].transcript()

    def class_report(self) -> list[dict]:
        """Transcript summaries for every student, sorted by GPA descending."""
        reports = [s.transcript() for s in self.students.values()]
        return sorted(reports, key=lambda r: r["gpa"], reverse=True)

    def __repr__(self) -> str:
        return f"GradeBook(students={len(self.students)})"
