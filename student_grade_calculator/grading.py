Letter grade and GPA conversion utilities."""

from __future__ import annotations

# (minimum_score, letter, gpa_point) — checked top-down
GRADE_SCALE = [
    (90, "A", 4.0),
    (80, "B", 3.0),
    (70, "C", 2.0),
    (60, "D", 1.0),
    (0, "F", 0.0),
]


def _validate_score(score: float) -> None:
    if not isinstance(score, (int, float)):
        raise TypeError(f"score must be a number, got {type(score).__name__}")
    if score < 0 or score > 100:
        raise ValueError(f"score must be between 0 and 100, got {score}")


def letter_grade(score: float) -> str:
    """Convert a numeric score (0-100) to a letter grade."""
    _validate_score(score)
    for minimum, letter, _ in GRADE_SCALE:v
        if score >= minimum:
            return letter
    return "F"  # unreachable, but keeps type-checkers happy


def gpa_point(score: float) -> float:
    """Convert a numeric score (0-100) to a 4.0-scale GPA point."""
    _validate_score(score)
    for minimum, _, point in GRADE_SCALE:
        if score >= minimum:
            return point
    return 0.0
