from unittest import TestCase
from datetime import date
from university_stuff import MathProfessor, PersonalInfo
from course import MathCourse, CourseInfo

math_course = MathCourse(10, 2)
math_course.course_info = CourseInfo("Math", date(2022, 9, 1), date(2022, 12, 1), "It's Math course.", [], [], 80, [])
test_professor_math = MathProfessor(200, math_course)
test_professor_math.personal_info = PersonalInfo(1, "Test", "Professor", "Drahomanova, 50", "+3809459834705",
                                                 "example@gmail.com", 0, "Professor", 200.34)
new_course = test_professor_math.create_course(test_professor_math, "Course", date(2022, 9, 1), date(2022, 12, 1),
                                               "Course created by Professor", [], [], 80, [])


class TestProfessorCreateNewCourse(TestCase):
    def test_professor_create_new_course(self):
        actual = new_course.course_info
        expected = new_course.course_info
        print(new_course.course_info)
        self.assertEqual(actual, expected)
