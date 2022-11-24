from threading import Lock
from Route import Route
import datetime


class ScheduleMeta(type):
    _instances = {}
    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
            return cls._instances[cls]


class Schedule(metaclass=ScheduleMeta):
    """Class represents schedule of tickets

    Arguments:
        tickets (list): Tickets for which we want to create schedule.

    Methods:
        create_schedule () -> None:
            Creates string of schedule based on tickets.

    """
    def __init__(self, tickets: list):
        self.tickets = tickets
        self.schedule = []

    def create_schedule(self, tickets: list) -> None:
        for ticket in tickets:
            self.tickets.append(ticket)

            now = datetime.datetime.now().replace(second=0, microsecond=0)

            route = Route(ticket.ticket_info.start_point, ticket.ticket_info.finish_point)
            route_info = route.route_info()

            new_schedule = {"departure": now, "arrive": now + datetime.timedelta(hours=route_info[1]),
                            "point_a": route_info[2], "point_b": route_info[3], "distance": route_info[0]}
            self.schedule.append(new_schedule)
