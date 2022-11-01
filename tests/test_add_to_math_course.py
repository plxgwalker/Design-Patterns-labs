from unittest import TestCase
from datetime import date
from university_stuff import Student, PersonalInfo
from course import MathCourse, CourseInfo

test_student = Student(0.3, False)
test_student.personal_info = PersonalInfo(0, "Test", "Student", "test street", "+2806369873242", "example@gmail.com", 1,
                                          "Student", 0)

math_course = MathCourse(12, 2)
math_course.course_info = CourseInfo("Math", date(2022, 9, 1), date(2022, 12, 1), "It's Math course.", [], [], 80, [])


class TestAddToMathCourse(TestCase):
    def test_add_to_math_course(self):
        math_course.add_student(test_student.personal_info.id)
        actual = math_course.course_info.students_list
        expected = [0]
        self.assertEqual(actual, expected)
