import datetime

from university_stuff import Student, Professor, PersonalInfo, Staff, split_full_name
from course import Course, CourseProgress

if __name__ == "__main__":
    test_student = Student(0.3, False)
    test_student.personal_info = PersonalInfo(0, "Test", "Student", "test street",
                                              "+2806369873242", "example@gmail.com", 1, "Student", 0)

    print(f"{test_student.personal_info}\n{test_student}")
