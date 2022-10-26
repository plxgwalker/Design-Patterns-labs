from __future__ import annotations
from typing import Dict, List, TYPE_CHECKING, Any
from datetime import datetime, date

if TYPE_CHECKING:
    from university_stuff import Student, Professor


class CourseProgress:
    """Represents progress of the course.

    Args:
        received_marks (dict): marks which received student.
        visited_lectures (int): how much lectures student have visited.
        completed_assignments (dict): completed assignments of student. 
        notes (dict): notes which have taken student.

    Methods:
        get_progress_to_date(date: datetime)
           Returns marks of the student.

        get_final_mark()
            Returns total float mark.

        fill_notes(note: str)
            Adding note to the dictionary "notes"

        remove_note(date: datetime)
            Removing note from dictionary "notes" by the date

    """

    def __init__(self, received_marks: dict, visited_lectures: int,
                 completed_assignments: dict, notes: dict):
        self.received_marks = received_marks
        self.visited_lectures = visited_lectures
        self.completed_assignments = completed_assignments
        self.notes = notes

    def get_progress_to_date(self, date: datetime) -> list:
        """Returning marks of the student

        Args:
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
        """Returning final mark of student

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


class Course:
    """Represents course.

    Args:
        title (str): title of the Course,
        start_date (datetime): start date of the course.
        end_date (datetime): end date of the course.
        description (str): description of the course.
        lectures (list[str]): list of lectures.
        assignments (list[str]): list of assignments.
        limit (int): limit of accepted students.
        students_list (list[int]): list of student's id's.

    """
    def __init__(self, title: str, start_date: datetime, end_date: datetime,
                 description: str, lectures: list[str], assignments: list[str],
                 limit: int, students_list: list[int], seminars: list[str]):
        self.title = title
        self.start_date = start_date
        self.end_date = end_date
        self.description = description
        self.lectures = lectures
        self.assignments = assignments
        self.limit = limit
        self.students_list = students_list
        self.seminars = seminars


class Seminar:
    def __init__(self, _id: int, title: str, deadline: datetime,
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

            Args:
                self

            Returns:
                None

            Raises:
                ValueError: If 'Student' has already been enrolled in this 'Course'.

        """
        if self.student.personal_info.id in self.course.students_list:
            raise ValueError("Student has already enrolled.")
        else:
            self.course.students_list.append(self.student.personal_info.id)

    def unenroll(self) -> None:
        """Unenrollment function.

            Args:
                self

            Returns:
                None

            Raises:
                ValueError: If 'Student' does not exists in this 'Course'.

        """
        if self.student.personal_info.id in self.course.students_list:
            self.course.students_list.remove(self.student.personal_info.id)
        else:
            raise ValueError("Student does not exists in this course.")
