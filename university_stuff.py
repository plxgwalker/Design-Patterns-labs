from __future__ import annotations

import abc
from typing import Dict, List, TYPE_CHECKING
from datetime import datetime
from dataclasses import dataclass
from abc import ABC, abstractmethod
if TYPE_CHECKING:
    from course import Course, CourseProgress


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


@property
def split_full_name(phrase: str) -> None:
    splitted_full_name = phrase.split()
    PersonalInfo.first_name = splitted_full_name[0]
    PersonalInfo.second_name = splitted_full_name[1]


class Staff(ABC):
    def __init__(self) -> None:
        self._personal_info = 0

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
    def personal_info(self):
        return self._personal_info, self.average_mark, self.courses

    def personal_info(self, personal_info: PersonalInfo,
                      average_mark: float, courses: list) -> None:
        if isinstance(personal_info, PersonalInfo):
            self._personal_info = personal_info
            self.average_mark = average_mark
            self.courses = courses

    def send_request(self, destination: Department) -> bool:
        pass

    def ask_sick_leave(self, department: Department) -> bool:
        pass


class PostgraduateStudent(Staff):
    def personal_info(self):
        return self._personal_info, self.average_mark, self.courses, self.phd_status

    def personal_info(self, personal_info: PersonalInfo,
                      average_mark: float, courses: list, phd_status: bool) -> None:
        if isinstance(personal_info, PersonalInfo):
            self._personal_info = personal_info
            self.average_mark = average_mark
            self.courses = courses
            self.phd_status = phd_status

    def send_request(self, destination: Department) -> bool:
        pass

    def ask_sick_leave(self, department: Department) -> bool:
        pass


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
