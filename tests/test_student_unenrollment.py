from unittest import TestCase
from datetime import date
from university_stuff import Student, PersonalInfo
from course import MathCourse, CourseInfo, Enrollment

test_student = Student(0.3, False)
test_student.personal_info = PersonalInfo(0, "Test", "Student", "test street", "+2806369873242", "example@gmail.com", 1,
                                          "Student", 0)

math_course = MathCourse(12, 2)
math_course.course_info = CourseInfo("Math", date(2022, 9, 1), date(2022, 12, 1), "It's Math course.", [], [], 80, [0])

enrollment_to_math = Enrollment(test_student, math_course)


class TestUnEnrollment(TestCase):
    def test_unenrollment(self):
        enrollment_to_math.unenroll()
        actual = math_course.course_info.students_list
        expected = []
        self.assertEqual(actual, expected)
