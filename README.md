README.md
# student-grade-calculator

A small, dependency-free Python library for computing student grades
across **multiple students and multiple courses**. Supports simple
averages, weighted averages, letter grades (A-F), and GPA (4.0 scale).

## Install (editable/local)

```bash
git clone https://github.com/<your-username>/student-grade-calculator.git
cd student-grade-calculator
pip install -e .
Quick start
from student_grade_calculator import GradeBook

gb = GradeBook()
gb.add_student("S001", "Ama Mensah")
gb.add_student("S002", "Kwame Owusu")

# Weighted scores: (assessment, score, weight)
gb.add_score("S001", "Math101", "Midterm", 78, weight=0.4)
gb.add_score("S001", "Math101", "Final", 85, weight=0.6)

gb.add_score("S002", "Math101", "Midterm", 60, weight=0.4)
gb.add_score("S002", "Math101", "Final", 70, weight=0.6)

print(gb.student_report("S001"))
# {'student_id': 'S001', 'name': 'Ama Mensah', 'gpa': 3.0,
#  'courses': {'Math101': {'average': 82.0, 'letter_grade': 'B'}}}

print(gb.class_average("Math101"))   # 75.0
print(gb.top_student("Math101"))     # Student(id='S001', ...)
print(gb.class_report())             # every student, sorted by GPA desc
Grading scale
Score	Letter	GPA
90-100	A	4.0
80-89	B	3.0
70-79	C	2.0
60-69	D	1.0
0-59	F	0.0
API overview
Course — tracks assessments/scores/weights for one course, computes simple_average(), weighted_average(), letter_grade(), gpa().
Student — a student enrolled in multiple Courses; computes overall gpa() and transcript().
GradeBook — the class-wide container: add_student, add_score, class_average, top_student, student_report, class_report.
Running tests
pip install -e ".[dev]"
pytest
License
MIT

---

## File 4 of 12: `pyproject.toml`

```toml
[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"

[student_grade_calculator]
name = "student-grade-calculator"
version = "0.1.0"
description = "A small library for computing weighted/simple averages, letter grades, and GPA across multiple students and courses."
readme = "README.md"
requires-python = ">=3.9"
license = { text = "MIT" }
authors = [
    { name = "Sarah Ama Brew" }
]
classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
]

[project.optional-dependencies]
dev = ["pytest>=7.0"]

[tool.setuptools.packages.find]
include = ["student_grade_calculator*"]
