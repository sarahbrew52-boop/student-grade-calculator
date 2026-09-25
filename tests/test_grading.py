import pytest
from student_grade_calculator.grading import letter_grade, gpa_point


@pytest.mark.parametrize("score,expected", [
    (95, "A"), (90, "A"),
    (89, "B"), (80, "B"),
    (79, "C"), (70, "C"),
    (69, "D"), (60, "D"),
    (59, "F"), (0, "F"),
])
def test_letter_grade(score, expected):
    assert letter_grade(score) == expected


@pytest.mark.parametrize("score,expected", [
    (95, 4.0), (85, 3.0), (75, 2.0), (65, 1.0), (30, 0.0),
])
def test_gpa_point(score, expected):
    assert gpa_point(score) == expected


def test_invalid_score_raises():
    with pytest.raises(ValueError):
        letter_grade(150)
    with pytest.raises(ValueError):
        gpa_point(-5)
