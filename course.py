from __future__ import annotations
from typing import Dict, List, TYPE_CHECKING
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

    def get_progress_to_date(self, date: datetime) -> str:
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
        today_date = date.today()
        self.notes[today_date] = note

    def remove_note(self, date: date) -> None:
        del self.notes[date]


class Course:
    def __init__(self, title: str, start_date: datetime, end_date: datetime,
                 description: str, lectures: list[str], assignments: list[str],
                 limit: int, students_list: list[int]):
        self.title = title
        self.start_date = start_date
        self.end_date = end_date
        self.description = description
        self.lectures = lectures
        self.assignments = assignments
        self.limit = limit
        self.students_list = students_list

    def add_student(self, student: Student) -> None:
        try:
            student.enroll(course=self)
        except ValueError:
            print(
                f"Student id: {student.student_id} has already enrolled to {self.title}.")

    def remove_student(self, student: Student) -> None:
        try:
            student.unenroll(course=self)
        except ValueError:
            print(
                f"Student id: {student.student_id} has already unenrolled to {self.title}.")
