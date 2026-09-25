import pytest
from student_grade_calculator import GradeBook


@pytest.fixture
def gb():
    book = GradeBook()
    book.add_student("S001", "Ama Mensah")
    book.add_student("S002", "Kwame Owusu")
    book.add_score("S001", "Math101", "Final", 90, weight=1.0)
    book.add_score("S002", "Math101", "Final", 70, weight=1.0)
    return book


def test_class_average(gb):
    assert gb.class_average("Math101") == 80.0


def test_top_student(gb):
    top = gb.top_student("Math101")
    assert top.student_id == "S001"


def test_unknown_student_raises(gb):
    with pytest.raises(KeyError):
        gb.add_score("S999", "Math101", "Final", 50)


def test_class_report_sorted_by_gpa(gb):
    report = gb.class_report()
    assert report[0]["student_id"] == "S001"
    assert report[1]["student_id"] == "S002"
