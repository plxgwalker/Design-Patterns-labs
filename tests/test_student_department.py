from unittest import TestCase
from university_stuff import Student, PersonalInfo, Department

test_student = Student(0.3, False)
test_student.personal_info = PersonalInfo(0, "Test", "Student", "test street",
                                          "+2806369873242", "example@gmail.com", 1, "Student", 0)
LNU = Department("LNU", [test_student.personal_info.id], [], ["Math"], [None])


class TestDepartment(TestCase):

    def test_department(self):
        actual = LNU.students
        expected = [0]
        self.assertEqual(actual, expected)
