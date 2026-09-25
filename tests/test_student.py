from student_grade_calculator import Course, Student


def test_course_simple_average():
    c = Course("Math101")
    c.add_score("Quiz1", 80)
    c.add_score("Quiz2", 90)
    assert c.simple_average() == 85.0


def test_course_weighted_average():
    c = Course("Math101")
    c.add_score("Midterm", 70, weight=0.4)
    c.add_score("Final", 90, weight=0.6)
    assert round(c.weighted_average(), 2) == 82.0


def test_course_weighted_falls_back_to_simple_when_no_weights():
    c = Course("Math101")
    c.add_score("Quiz1", 60)
    c.add_score("Quiz2", 80)
    assert c.weighted_average() == c.simple_average() == 70.0


def test_student_multi_course_gpa():
    s = Student("S001", "Ama Mensah")
    s.add_score("Math101", "Final", 95)   # A -> 4.0
    s.add_score("Eng101", "Final", 75)    # C -> 2.0
    assert s.gpa() == 3.
