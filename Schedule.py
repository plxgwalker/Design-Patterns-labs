from threading import Lock
from Route import Route
import datetime

# from Depo import Depo, DepoInfo


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
        self.schedule = "Schedule:\n"

    def create_schedule(self) -> None:
        for ticket in self.tickets:
            now = datetime.datetime.now().replace(second=0, microsecond=0)
            route = Route(ticket.ticket_info.start_point, ticket.ticket_info.finish_point)
            route_info = route.route_info(ticket)
            self.schedule += f"\nDeparture: {now} Arrive: {now + datetime.timedelta(hours=route_info[1])} " \
                             f"{route_info[2]} -> {route_info[3]} Distance: {route_info[0]}"


# if __name__ == "__main__":
#     test_depo = Depo()
#     test_depo_info = DepoInfo(1, "Lviv", [], [], [], [])
#     test_depo.depo_info = test_depo_info
#
#     test_depo.create_tickets("Kyiv", 2, "Bus")
#
#     test_schedule = Schedule(test_depo.depo_info.tickets)
#     test_schedule.create_schedule()
#     print(test_schedule.schedule)
