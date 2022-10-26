import datetime
from unittest import TestCase
from course import Course, Seminar

Math = Course("Math", datetime.datetime(2022, 9, 1), datetime.datetime(2023, 6, 1),
              "lorem ipsum.", [" "], [" "], 80, [], [])
seminar_math_0 = Seminar(0, "lorem ipsum.", datetime.datetime(2022, 9, 1), [], None, Math.title)


class TestCourseSeminar(TestCase):

    def test_course_seminar(self):
        Math.seminars.append(seminar_math_0.title)
        actual = Math.seminars
        expected = ["lorem ipsum."]
        self.assertEqual(actual, expected)
