import datetime

from university_stuff import Student, Professor
from course import Course, CourseProgress

if __name__ == "__main__":
    test_student = Student("Test Student", "Drahomanova, 50", "+380000000007",
                           "test.student@lnu.edu.com", 1, 2.2, ["Math", "OOP"])
    test_course = Course("Test Course", 2022-9-1, 2023-6-30,
                         "lorem impsum.", ["lecture_1"], [], 80, [])
    test_professor = Professor(
        "Test Professor", "Drahomanova 50", "+380000002", "test.professor@lnu.edu.ua", 500)
    assignment_0 = {datetime.datetime(2022, 9, 1): {"title": "Math",
                             "is_done": True, "description": "lorem impsum.", "mark": 0}}
    test_course_progress = CourseProgress({}, 1, assignment_0, {})

    # Test of Student's methods
    print(test_student.taken_courses(self=test_student))
    test_student.enroll(test_course)
    print(test_student.taken_courses(self=test_student))
    test_student.unenroll(test_course)  # BUG
    print(test_student.taken_courses(self=test_student))

    # Test of Professor's method
    print(f"\n{assignment_0}")
    test_professor.check_assignment(assignment_0, test_course_progress)
    print(f"{assignment_0}")

    # Test of CourseProgress.get_progress and final mark methods
    print(f"\n{test_course_progress.get_progress_to_date(datetime.datetime(2022, 9, 30))}")
    print(f"{test_course_progress.get_final_mark()}")

    # Test of CourseProgress.notes methods
    test_course_progress.fill_notes("Test note.")
    print(f"\n{test_course_progress.notes}")
    test_course_progress.remove_note(datetime.date(2022, 9, 30))
    print(f"{test_course_progress.notes}")

    # Test of Curse methods
    print(f"\n{test_course.students_list}")
    test_course.remove_student(test_student)  # BUG
    print(f"{test_course.students_list}")