from Ticket import Ticket, TicketInfo
from dataclasses import dataclass


@dataclass
class PassengerInfo:
    """Represents dataclass of information about 'Passenger'.

    Arguments:
        id (int): ID of 'Passenger'.
        f_name (str): First name of 'Passenger'.
        l_name (str): Last name of 'Passenger'.
        age (int): Age of 'Passenger'.

    """
    id: int
    f_name: str
    l_name: str
    age: int
    tickets: list[Ticket]


class Passenger:
    """Represents class 'Passenger'.

    Properties:
        @property
        passenger_info ():
            Returns parameter '_passenger_info'.

        @passenger_info.setter
        passenger_info (passenger_info: PassengerInfo):
            Setting parameter '_passenger_info' values of 'passenger_info'.

    Methods:
        add_ticket (ticket: Ticket) -> str:
            Adding ticket with current ID to Passenger portfolio if there is no ticket with that ID.

        cancel (ticket: Ticket) -> str:
            Cancelling ticket with current ID from Passenger portfolio if ticket with this ID exists.

    Returns:
        add_ticket (ticket: Ticket) -> str:
            String if adding successful.

        cancel_ticket (ticket: Ticket) -> str:
            String if cancelling successful.

    Raises:
        add_ticket (ticket: Ticket) -> str:
            ValueError: If there is no ticket with that ID.

        cancel_ticket (ticket: Ticket) -> str:
            ValueError: If ticket with this ID exists.

    """
    def __init__(self) -> None:
        self._passenger_info = None

    @property
    def passenger_info(self):
        return self._passenger_info

    @passenger_info.setter
    def passenger_info(self, passenger_info: PassengerInfo) -> None:
        if isinstance(passenger_info, PassengerInfo):
            self._passenger_info = passenger_info

    def add_ticket(self, ticket: Ticket) -> str:
        if ticket.ticket_info.id in self._passenger_info.tickets:
            raise ValueError(f"Ticket with this ID has already added.")
        else:
            self._passenger_info.tickets.append(ticket.ticket_info.id)
            return f"Added new ticket with ID: {ticket.ticket_info.id}"

    def cancel_ticket(self, ticket: Ticket) -> str:
        if ticket.ticket_info.id in self._passenger_info.tickets:
            self._passenger_info.tickets.remove(ticket.ticket_info.id)
            return f"Ticket with ID: {ticket.ticket_info.id} has been removed."
        else:
            raise ValueError(f"No ticket with this ID in your tickets")
