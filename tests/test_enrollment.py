import datetime
from unittest import TestCase
from university_stuff import Student, PersonalInfo
from course import Course, Enrollment

test_student = Student(4.5, False)
test_student.personal_info = PersonalInfo(1, "Test", "Student", "test street", "+2806369873242",
                                          "example@gmail.com", 1, "Student", 0)
math_course = Course("Math", datetime.datetime(2022, 9, 1), datetime.datetime(2023, 6, 1), "lorem ipsum.",
                     [" "], [" "], 80, [], [])


class TestEnrollment(TestCase):

    def test_enrollment(self):
        enrollment_to_math_course = Enrollment(test_student, math_course)
        enrollment_to_math_course.enroll()
        actual = math_course.students_list
        expected = [1]
        self.assertEqual(actual, expected)
