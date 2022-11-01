from __future__ import annotations

import abc
from typing import TYPE_CHECKING, Any, Type
from datetime import datetime
from dataclasses import dataclass
from abc import ABC, abstractmethod
from course import Course, CourseInfo, CourseProgress


@dataclass
class PersonalInfo:
    id: int
    first_name: str
    second_name: str
    address: str
    phone_number: str
    email: str
    position: int
    rank: str
    salary: float

    def __str__(self):
        return f"ID: {self.id}\nFirst name: {self.first_name}\n" \
               f"Second name: {self.second_name}\nAddress: {self.address}\n" \
               f"Phone number: {self.phone_number}\nEmail: {self.email}\n" \
               f"Position: {self.position}\nRank: {self.rank}\nSalary: {self.salary}"


@property
def split_full_name(phrase: str) -> None:
    splitted_full_name = phrase.split()
    PersonalInfo.first_name = splitted_full_name[0]
    PersonalInfo.second_name = splitted_full_name[1]


@dataclass
class Group:
    id: int
    title: str
    students_list: list
    department_id: int


class Staff(ABC):
    def __init__(self) -> None:
        self._personal_info = None

    @property
    def personal_info(self):
        return self._personal_info

    @personal_info.setter
    def personal_info(self, personal_info: PersonalInfo) -> None:
        if isinstance(personal_info, PersonalInfo):
            self._personal_info = personal_info

    @abstractmethod
    def ask_sick_leave(self, department: Department) -> bool:
        pass

    @abstractmethod
    def send_request(self, department: Department) -> bool:
        pass


class Student(Staff):
    def __init__(self, average_mark: float, phd_status: bool) -> None:
        super().__init__()
        self.average_mark = average_mark
        self.phd_status = phd_status

    def __str__(self):
        return f"Average mark: {self.average_mark}\nPHD status: {self.phd_status}"

    def send_request(self, destination: Department) -> bool:
        pass

    def ask_sick_leave(self, department: Department) -> bool:
        pass


class PostgraduateStudent(Staff):
    def __init__(self, average_mark: float, phd_status: bool) -> None:
        super().__init__()
        self.average_mark = average_mark
        self.phd_status = phd_status

    def __str__(self):
        return f"Average mark: {self.average_mark}\nPHD status: {self.phd_status}"

    def send_request(self, destination: Department) -> bool:
        pass

    def ask_sick_leave(self, department: Department) -> bool:
        pass


class Professor(Staff):
    def __init__(self, salary: float, related_course: Course) -> None:
        super().__init__()
        self.salary = salary
        self.related_course = related_course

    @abstractmethod
    def fill_course(self, group: Group, *args):
        for i in group.students_list:
            self.related_course.add_student(i)

    @abstractmethod
    def create_course(self, *args):
        new_course = Course
        new_course.course_info = CourseInfo(args[0], args[1], args[2], args[3], args[4], args[5], args[6], args[7])
        return new_course

    def ask_sick_leave(self, department: Department) -> bool:
        pass

    def send_request(self, department: Department) -> bool:
        pass

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


class MathProfessor(Professor):
    def fill_course(self, group: Group, *args):
        for student in group.students_list:
            self.related_course.add_student(student)

    def create_course(self, *args):
        new_course = Course
        new_course.course_info = CourseInfo(args[0], args[1], args[2], args[3], args[4], args[5], args[6], args[7])
        return new_course


class Department:
    def __init__(self, department_id: int, title: str, students: list[Student], professors: list[Professor],
                 courses: list[str], requests: list[Any]):
        self.department_id = department_id
        self.title = title
        self.students = students
        self.professors = professors
        self.courses = courses
        self.requests = requests

    def __str__(self):
        return f"Department title: {self.title}\nStudents: {self.students}" \
               f"\nProfessors: {self.professors}\nCourses: {self.courses}" \
               f"\nRequests: {self.requests}"

    def proceed_requests(self) -> Any:
        pass
