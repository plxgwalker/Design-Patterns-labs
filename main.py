import datetime

from university_stuff import Student, Professor, PersonalInfo, Department
from course import Course, Seminar, Enrollment

if __name__ == "__main__":
    """Place for testing"""

    # Initializing all classes.
    test_student = Student(0.3, False)
    test_student.personal_info = PersonalInfo(0, "Test", "Student", "test street",
                                              "+2806369873242", "example@gmail.com", 1, "Student", 0)
    LNU = Department("LNU", [test_student.personal_info.id], [], ["Math"], [None])
    Math = Course("Math", datetime.datetime(2022, 9, 1), datetime.datetime(2023, 6, 1),
                  "lorem ipsum.", [" "], [" "], 80, [], [])
    seminar_math_0 = Seminar(0, "lorem ipsum.", datetime.datetime(2022, 9, 1), [], None, Math.title)

    # Student and Department info.
    print(f"{test_student.personal_info}\n{test_student}\n")
    print(LNU)

    # Enrollment/unenrollment.
    enrollment_to_math = Enrollment(test_student, Math)
    print(f"\n{Math.students_list}")
    enrollment_to_math.enroll()
    print(f"{Math.students_list}")
    enrollment_to_math.unenroll()
    print(f"{Math.students_list}")

    # Seminar and Course.
    print(seminar_math_0)
    Math.seminars = seminar_math_0.title
    print(f"\nCourse seminars: {Math.seminars}")
