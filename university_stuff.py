from __future__ import annotations
from typing import Dict, List, TYPE_CHECKING
from datetime import datetime
if TYPE_CHECKING:
    from course import Course, CourseProgress


class Student:
    """
    A class Student represents student of university.

    Args:
        full_name (str): full name of student.
        address (str): address where living student.
        phone_number (str): phone number of student.
        email (str): email of student.
        student_id (int): id of student.
        average_mark (float): arithmetic mean of student.

    Methods:
        enroll(course: Course)
            Adding student to the course. Returns nothing.

        unenroll(course: Course)
            Kicking student from course.

    """

    def __init__(self, full_name: str, address: str, phone_number: str,
                 email: str, student_id: int, average_mark: float, courses: list):
        """
        Parameters:
            full_name (str): full name of student.
            address (str): address where living student.
            phone_number (str): phone number of student.
            email (str): email of student.
            student_id (int): id of student.
            average_mark (float): arithmetic mean of student.
            courses (list): list of student's courses.

        """
        self.full_name = full_name
        self.address = address
        self.phone_number = phone_number
        self.email = email
        self.student_id = student_id
        self.average_mark = average_mark
        self.courses = courses

    @staticmethod
    def taken_courses(self) -> list:
        """Returning courses which has student

        Returns:
            List of student's courses.

        """
        return self.courses

    def enroll(self, course: Course) -> None:
        """Enroll student to course

        Args:
            course (Course): the course to which we are wanting to add student.

        Returns:
            Nothing.

        Raises:
            ValueError: If "x.title" hasn't mentioned in "self.courses"

        """
        for x in self.courses:
            if x.title == course.title:
                raise ValueError("Course has already enrolled.")
                break
            else:
                self.courses.append(course.title)
                course.students_list.append(self.student_id)
                print(
                    f"Student id: {self.student_id} has enrolled to {course.title}")
                break

    def unenroll(self, course: Course) -> None:
        """Unenroll student from course

            Args:
                course (Course): the course from which we are wanting to unenroll student.

            Returns:
                Nothing.

            Raises:
                ValueError: If "x.title" hasn't mentioned in "self.courses"

        """
        for x in self.courses:
            if x.title == course.title:
                self.courses.remove(course.title)
                course.students_list.remove(self.student_id)
                print(
                    f"Student id: {self.student_id} has unenrolled from {course.title}")
                break
            else:
                print(
                    f"Student id: {self.student_id} has already been unenrolled from {course.title}")
                break


class Professor:
    """Class professor represents professor of university.

    Args:
        full_name (str): full name of professor.
        address (str): address where professor currently living.
        phone_number (str): phone number of professor.
        email (str): email of student.
        salary (float): salary of professor.

    """

    def __init__(self, full_name: str, address: str, phone_number: str, email: str, salary: float):
        self.full_name = full_name
        self.address = address
        self.phone_number = phone_number
        self.email = email
        self.salary = salary

    @staticmethod
    def check_assignment(assignment: dict, course_progress: CourseProgress) -> None:
        """Checking if student has made an assignment

        If dictionary has value "True", then we are type mark "5"

        Args:
            assignment (dict): dictionary of student's assignment.
            Assignment dictionary structure:
                {"title": str, "is_done": bool, "description": str, "mark": float}

        Returns:
            Nothing.

        """
        for key, value in assignment.items():
            if value["is_done"]:
                value["mark"] = 5
            if key:
                course_progress.received_marks.update({"datetime": 5})
