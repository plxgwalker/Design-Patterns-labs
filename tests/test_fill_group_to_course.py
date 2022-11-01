from unittest import TestCase
from datetime import date
from university_stuff import MathProfessor, Student, PersonalInfo, Group, Department
from course import MathCourse, CourseInfo

# Course
math_course = MathCourse(10, 2)
math_course.course_info = CourseInfo("Math", date(2022, 9, 1), date(2022, 12, 1), "It's Math course.", [], [], 80, [])

# Student
test_student = Student(0.3, False)
test_student.personal_info = PersonalInfo(0, "Test", "Student", "test street", "+2806369873242", "example@gmail.com", 1,
                                          "Student", 0)

# Math Professor
test_professor_math = MathProfessor(200, math_course)
test_professor_math.personal_info = PersonalInfo(1, "Test", "Professor", "Drahomanova, 50", "+3809459834705",
                                                 "example@gmail.com", 0, "Professor", 200.34)

# Department
LNU = Department(0, "LNU", [test_student.personal_info.id], [], ["Math"], [None])

# Group
test_group = Group(0, "Test FeP-23", [0], LNU.department_id)


class TestFillGroupToCourse(TestCase):
    def test_fill_group_to_course(self):
        test_professor_math.fill_course(test_group)
        actual = math_course.course_info.students_list
        expected = [0]
        self.assertEqual(actual, expected)
