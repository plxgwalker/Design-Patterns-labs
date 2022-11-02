from __future__ import annotations
from typing import TYPE_CHECKING, Any
from datetime import datetime, date
from dataclasses import dataclass
from abc import ABC, abstractmethod

if TYPE_CHECKING:
    from university_stuff import Student


@dataclass
class GroupInfo:
    """Class represents information about 'Group'.

    Arguments:
        id (int): 'Group' id.
        title (str): 'Group' name.
        students_list (list): 'Group' list.
        department_id (int) Department id of a 'Group'.

    """
    id: int
    title: str
    student_list: list
    department_id: int


@dataclass
class CourseInfo:
    """Class represents information about 'Course'.

        Arguments:
            title (str): 'Course' name.
            start_date (date): Date of start 'Course'.
            end_date (date): Date of the end 'Course'.
            description (str): Information about 'Course'.
            lectures (list): List of lectures in 'Course'.
            assignments (list): List of assignments in 'Course'.
            limit (int): Student limit.
            students_list (list): List of students in 'Course'.

        Methods:
            __str__():
                Returns 'Course' info.

        Returns:
            __str__(): Returns 'Course' info.

        """
    title: str
    start_date: date
    end_date: date
    description: str
    lectures: list[str]
    assignments: list[str]
    limit: int
    students_list: list[int]

    def __str__(self) -> str:
        return f"Title: {self.title}\n" \
               f"Description: {self.description}\n" \
               f"Start date: {self.start_date}\n" \
               f"End date: {self.end_date}\n" \
               f"Lectures: {self.lectures}\n" \
               f"Assignments: {self.assignments}\n" \
               f"Student limit: {self.limit}\n" \
               f"Students list: {self.students_list}\n"


class CourseProgress:
    """Represents progress of the course.

    Arguments:
        received_marks (dict): marks which received student.
        visited_lectures (int): how much lectures student have visited.
        completed_assignments (dict): completed assignments of student. 
        notes (dict): notes which have taken student.

    Methods:
        get_progress_to_date(date: datetime):
           Returns marks of the student.

        get_final_mark():
            Returns total float mark.

        fill_notes(note: str):
            Adding note to the dictionary "notes".

        remove_note(date: datetime):
            Removing note from dictionary "notes" by the date.

    """

    def __init__(self, received_marks: dict, visited_lectures: int, completed_assignments: dict, notes: dict) -> None:
        self.received_marks = received_marks
        self.visited_lectures = visited_lectures
        self.completed_assignments = completed_assignments
        self.notes = notes

    def get_progress_to_date(self, date: datetime) -> list:
        """Returning marks of the student.

        Arguments:
            date (datetime): date due to which we want to take marks.

        Returns:
            Dictionary "marks" with structure: "task": "mark".

        """
        marks = []
        for k, x in self.completed_assignments.items():
            if k < date:
                marks.append(x["mark"])
        return marks

    def get_final_mark(self) -> float:
        """Returning final mark of student.

        Returns:
            Arithmetic mean of student for this course.

        """
        values = self.received_marks.values()
        amounts_of_marks = self.received_marks
        return sum(values) / len(amounts_of_marks)

    def fill_notes(self, note: str) -> None:
        """Adding new note to notes

        Args:
            note (str): note which we want to add.

        Returns:
            Nothing.

        """
        today_date = date.today()
        self.notes[today_date] = note

    def remove_note(self, date: date) -> None:
        """Deleting notes by the date.

        Args:
            date (date): date of the note we want to delete.

        Returns:
            Nothing.

        """
        del self.notes[date]


class Course(ABC):
    """Abstract class represents 'Course'.

    Methods:
        @property
        course_info ():
            Returns information about 'Course'.

        @course_info.setter
        course_info (course_info: CourseInfo) -> None:
            Setting information about 'Course'.

        @abstractmethod
        add_student(student: Student.personal_info.id) -> None:
            Adding 'Student' to 'Course'.

        @abstractmethod
        remove_student(student: Student.personal_info.id) -> None:
            Removes 'Student' from 'Course'.

    Raises:
        ValueError in add_student:
            If 'Student' already exists in 'Course'.

        ValueError in remove_student:
            If 'Student' does not exist in 'Course'.

    """
    def __init__(self) -> None:
        self._course_info = None

    @property
    def course_info(self) -> CourseInfo:
        return self._course_info

    @course_info.setter
    def course_info(self, course_info: CourseInfo) -> None:
        if isinstance(course_info, CourseInfo):
            self._course_info = course_info

    @abstractmethod
    def add_student(self, student: Student.personal_info.id) -> None:
        if student in self.course_info.students_list:
            raise ValueError(f"Student {student} already exists in this course.")
        else:
            self.course_info.students_list.append(student)

    @abstractmethod
    def remove_student(self, student: Student.personal_info.id) -> None:
        if student not in self.course_info.students_list:
            raise ValueError(f"Student {student} does not exists in this course.")
        else:
            self.course_info.students_list.remove(student)


class MathCourse(Course):
    """Class represents inheritance from 'Course'.

        Methods:
            add_student(student: Student.personal_info.id) -> None:
                Adding 'Student' to 'Course'.

            remove_student(student: Student.personal_info.id) -> None:
                Removes 'Student' from 'Course'.

        Raises:
            ValueError in add_student:
                If 'Student' already exists in 'Course'.

            ValueError in remove_student:
                If 'Student' does not exist in 'Course'.

        """
    def __init__(self, practice_classes: int, modules: int):
        super().__init__()
        self.practice_classes = practice_classes
        self.modules = modules

    def __str__(self):
        return f"Course info: {self.course_info}" \
               f"\nMath course classes: {self.practice_classes}, Modules: {self.modules}"

    def add_student(self, student: Student.personal_info.id):
        if student in self.course_info.students_list:
            raise ValueError(f"Student {student} already exists in this course.")
        else:
            self.course_info.students_list.append(student)

    def remove_student(self, student: Student.personal_info.id):
        if student not in self.course_info.students_list:
            raise ValueError(f"Student {student} does not exists in this course.")
        else:
            self.course_info.students_list.remove(student)


class ProgrammingCourse(Course):
    """Class represents inheritance from 'Course'.

        Methods:
            add_student(student: Student.personal_info.id) -> None:
                Adding 'Student' to 'Course'.

            remove_student(student: Student.personal_info.id) -> None:
                Removes 'Student' from 'Course'.

        Raises:
            ValueError in add_student:
                If 'Student' already exists in 'Course'.

            ValueError in remove_student:
                If 'Student' does not exist in 'Course'.

    """
    def __init__(self, patterns: int, modules: int):
        super().__init__()
        self.patterns = patterns
        self.modules = modules

    def __str__(self):
        return f"Course info: {self.course_info}" \
               f"\nProgramming course patterns: {self.patterns}, Modules: {self.modules}"

    def add_student(self, student: Student.personal_info.id):
        if student in self.course_info.students_list:
            raise ValueError(f"Student {student} already exists in this course.")
        else:
            self.course_info.students_list.append(student)

    def remove_student(self, student: Student.personal_info.id):
        if student not in self.course_info.students_list:
            raise ValueError(f"Student {student} does not exists in this course.")
        else:
            self.course_info.students_list.remove(student)


class AlgorithmCourse(Course):
    """Class represents inheritance from 'Course'.

        Methods:
            add_student(student: Student.personal_info.id) -> None:
                Adding 'Student' to 'Course'.

            remove_student(student: Student.personal_info.id) -> None:
                Removes 'Student' from 'Course'.

        Raises:
            ValueError in add_student:
                If 'Student' already exists in 'Course'.

            ValueError in remove_student:
                If 'Student' does not exist in 'Course'.

        """
    def __init__(self, algorithms: int, modules: int):
        super().__init__()
        self.algorithms = algorithms
        self.modules = modules

    def __str__(self):
        return f"Course info: {self.course_info}" \
               f"\nProgramming course patterns: {self.algorithms}, Modules: {self.modules}"

    def add_student(self, student: Student.personal_info.id):
        if student in self.course_info.students_list:
            raise ValueError(f"Student {student} already exists in this course.")
        else:
            self.course_info.students_list.append(student)

    def remove_student(self, student: Student.personal_info.id):
        if student not in self.course_info.students_list:
            raise ValueError(f"Student {student} does not exists in this course.")
        else:
            self.course_info.students_list.remove(student)


class Seminar:
    """Class represents seminar for 'Course'.

    Arguments:
        _id (int): id of 'Seminar'.
        title (str): Title of 'Seminar'.
        deadline (date): Deadline of 'Seminar'.
        assignments (list): List of 'Seminar' assignments.
        status (Any): Status of 'Seminar'.
        related_course (str): 'Course' of 'Seminar'.

    Methods:
        implement_item(item_name: str) -> None:
            Pass.

        add_comment(comment: str) -> None:
            Pass.
    """
    def __init__(self, _id: int, title: str, deadline: date,
                 assignments: list[dict], status: Any, related_course: str) -> None:
        self.id = _id
        self.title = title
        self.deadline = deadline
        self.assignments = assignments
        self.status = status
        self.related_course = related_course

    def __str__(self):
        return f"\nSeminar id: {self.id} \nSeminar title: {self.title} " \
               f"\nDeadline: {self.deadline} \nAssignments: {self.assignments}" \
               f"\nStatus: {self.status} \nCourse: {self.related_course}"

    def implement_item(self, item_name: str) -> None:
        pass

    def add_comment(self, comment: str) -> None:
        pass


class Enrollment:
    """Represents enrollment 'Student' to 'Course'.

    Args:
        student (Student): 'Student' which have to be added to 'Course'.
        course (Course): 'Course' to which 'Student' have to be added.

    Methods:
        enroll ():
            Enrolling 'Student' to the 'Course'.

        unenroll ():
            Unenrolling 'Student' from the 'Course'.

    """

    def __init__(self, student: Student, course: Course):
        self.student = student
        self.course = course

    def enroll(self) -> None:
        """Enrollment function.

            Returns:
                None

            Raises:
                ValueError: If 'Student' has already been enrolled in this 'Course'.

        """
        if self.student.personal_info.id in self.course.course_info.students_list:
            raise ValueError("Student has already enrolled.")
        else:
            self.course.course_info.students_list.append(self.student.personal_info.id)

    def unenroll(self) -> None:
        """Unenrollment function.

            Returns:
                None

            Raises:
                ValueError: If 'Student' does not exists in this 'Course'.

        """
        if self.student.personal_info.id in self.course.course_info.students_list:
            self.course.course_info.students_list.remove(self.student.personal_info.id)
        else:
            raise ValueError("Student does not exists in this course.")
