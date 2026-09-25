"""Course-level score tracking and averaging."""

from __future__ import annotations

from .grading import letter_grade, gpa_point


class Course:
    """Holds assessment scores (and optional weights) for one course."""

    def __init__(self, name: str):
        self.name = name
        self._scores: dict[str, float] = {}
        self._weights: dict[str, float] = {}

    def add_score(self, assessment: str, score: float, weight: float | None = None) -> None:
        """Record a score for an assessment (e.g. 'Midterm', 'Final').

        weight is optional; if omitted the assessment is treated as
        equally weighted when weighted_average() normalizes weights.
        """
        if score < 0 or score > 100:
            raise ValueError(f"score must be between 0 and 100, got {score}")
        if weight is not None and weight < 0:
            raise ValueError("weight cannot be negative")
        self._scores[assessment] = score
        self._weights[assessment] = weight if weight is not None else 0.0

    def simple_average(self) -> float:
        """Unweighted mean of all recorded scores."""
        if not self._scores:
            return 0.0
        return sum(self._scores.values()) / len(self._scores)

    def weighted_average(self) -> float:
        """Weighted mean. Falls back to simple_average() if no weights given."""
        if not self._scores:
            return 0.0
        total_weight = sum(self._weights.values())
        if total_weight == 0:
            return self.simple_average()
        return sum(
            self._scores[a] * self._weights[a] for a in self._scores
        ) / total_weight

    def letter_grade(self) -> str:
        return letter_grade(self.weighted_average())

    def gpa(self) -> float:
        return gpa_point(self.weighted_average())

    def __repr__(self) -> str:
        return f"Course(name={self.name!r}, avg={self.weighted_average():.1f})"
