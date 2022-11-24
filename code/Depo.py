from dataclasses import dataclass
from Transport import Train, Bus, Truck
from Ticket import Ticket, TicketInfo
from Passenger import Passenger


@dataclass
class DepoInfo:
    """Represents dataclass of information about 'Depo'.

    Arguments:
        id (int): ID of 'Passenger'.
        city (str): City where 'Depo' located.
        trains (list[Train]): List of trains in 'Depo'.
        busses (list[Bus]): List of busses in 'Depo'.
        trucks (list[Truck]): List of trucks in 'Depo'.
        tickets (list[Ticket]): List of tickets available in this 'Depo'.

    """
    id: int
    city: str
    trains: list[Train]
    busses: list[Bus]
    trucks: list[Truck]
    tickets: list[Ticket]


class Depo:
    """Class represents 'Depo'.

    Properties:
        @property
        depo_info (): Returns parameter '_depo_info'.

        @passenger_info.setter
        depo_info (depo_info: DepoInfo):
            Setting parameter '_depo_info' values of 'depo_info'.

    Methods:
        create_tickets (finish_point: str, amount: int, transport_type: str) -> str:
            Creates tickets for current 'Depo' with parameters 'finish_point' 'amount', 'transport_type'.

        print_all_tickets () -> str:
            Prints all available tickets for current 'Depo'.

        buy_ticket (passenger: Passenger) -> str:
            'Passenger' buys last ticket from 'Depo' 'tickets' list.

    Returns:
        create_tickets (finish_point: str, amount: int, transport_type: str) -> str:
            Information about tickets.

        print_all_tickets () -> str:
            All tickets from 'Depo' list 'tickets'.

        buy_ticket (passenger: Passenger) -> str:
            Message of successful sell.

    """
    def __init__(self):
        self._depo_info = None

    @property
    def depo_info(self) -> str:
        return self._depo_info

    @depo_info.setter
    def depo_info(self, depo_info: DepoInfo) -> None:
        if isinstance(depo_info, DepoInfo):
            self._depo_info = depo_info

    def create_tickets(self, finish_point: str, amount: int, transport_type: str) -> str:
        for ticket_id in range(0, amount):
            new_ticket = Ticket()
            new_ticket_info = TicketInfo(ticket_id, self._depo_info.city, finish_point, transport_type)
            new_ticket.ticket_info = new_ticket_info
            self._depo_info.tickets.append(new_ticket)

        return f"Added tickets:\nAmount of tickets: {amount}\nFrom: {self._depo_info.city} to " \
               f"{finish_point}\nTransport type: {transport_type}"

    def print_all_tickets(self) -> str:
        result = f""
        if not self._depo_info.tickets:
            result += f"No tickets yet."
        else:
            for i in range(0, len(self._depo_info.tickets)):
                result += f"{self._depo_info.tickets[i].ticket_info}\n"
        return result

    def buy_ticket(self, passenger: Passenger) -> str:
        amount_of_tickets = len(self._depo_info.tickets)
        passenger.passenger_info.tickets.append(self._depo_info.tickets[amount_of_tickets-1].ticket_info.id)
        self._depo_info.tickets.remove(self._depo_info.tickets[amount_of_tickets-1])
        return f"Passenger has bought ticket with ID: {passenger.passenger_info.tickets}"
