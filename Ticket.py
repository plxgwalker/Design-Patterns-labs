from dataclasses import dataclass


@dataclass
class TicketInfo:
    """Represents information about 'Ticket'
    Arguments:
        id (int): ID of 'Ticket'.
        start_point (str): Start point of route.
        finish_point (str): Finish poit of route.
        transport_type (str): Type of transport.

    """
    id: int
    start_point: str
    finish_point: str
    transport_type: str


class Ticket:
    """Represents class 'Ticket'.

    Properties:
        @property
        ticket_info ():
            Returns parameter '_ticket_info'.

        @ticket_info.setter
        ticket_info (ticket_info: TicketInfo):
            Setting parameter '_ticket_info' values of 'ticket_info'.

    """
    def __init__(self) -> None:
        self._ticket_info = None

    @property
    def ticket_info(self):
        return self._ticket_info

    @ticket_info.setter
    def ticket_info(self, ticket_info: TicketInfo) -> None:
        if isinstance(ticket_info, TicketInfo):
            self._ticket_info = ticket_info
