from datetime import date
import datetime
from university_stuff import Student, Professor, PersonalInfo, Department, Group, MathProfessor
from course import MathCourse, ProgrammingCourse, AlgorithmCourse, CourseInfo, Seminar, Enrollment

if __name__ == "__main__":
    """Place for testing"""

    # Initializing all classes.
    test_student = Student(0.3, False)
    test_student.personal_info = PersonalInfo(0, "Test", "Student", "test street",
                                              "+2806369873242", "example@gmail.com", 1, "Student", 0)

    LNU = Department(0, "LNU", [test_student.personal_info.id], [], ["Math"], [None])

    math_course = MathCourse(10, 2)
    math_course.course_info = CourseInfo("Math", date(2022, 9, 1), date(2022, 12, 1), "It's Math course.", [], [], 80,
                                         [])

    programming_course = ProgrammingCourse(12, 2)
    programming_course.course_info = CourseInfo("Programming", date(2022, 9, 1), date(2022, 12, 1),
                                                "It's programming course.", [], [], 80, [])

    algorithm_course = AlgorithmCourse(7, 2)
    algorithm_course.course_info = CourseInfo("Algorithms", date(2022, 9, 1), date(2022, 12, 1),
                                              "It's algorithm course.", [], [], 80, [])

    seminar_math_0 = Seminar(0, "lorem ipsum.", date(2022, 9, 1), [], None,
                             math_course.course_info.title)

    test_professor_math = MathProfessor(200, math_course)

    test_group = Group(0, "Test FeP-23", [0], LNU.department_id)

    # Student and Department info.
    print(f"{test_student.personal_info}\n{test_student}\n")
    print(LNU)

    # Enrollment/unenrollment.
    enrollment_to_math = Enrollment(test_student, math_course)
    print(f"\n{math_course.course_info.students_list}")
    enrollment_to_math.enroll()
    print(f"{math_course.course_info.students_list}")
    enrollment_to_math.unenroll()
    print(f"{math_course.course_info.students_list}")

    # Add student/Remove student.
    math_course.add_student(test_student.personal_info.id)
    print(f"{math_course.course_info.students_list}")
    math_course.remove_student(test_student.personal_info.id)
    print(f"{math_course.course_info.students_list}")

    # Seminar and Course.
    print(seminar_math_0)
    math_course.seminars = seminar_math_0.title
    print(f"\nCourse seminars: {math_course.seminars}")

    # Course created by Professor.
    new_course = test_professor_math.create_course(test_professor_math, "Course", date(2022, 9, 1), date(2022, 12, 1),
                                                   "Course created by Professor", [], [], 80, [])
    print(f"\n{new_course.course_info}")
