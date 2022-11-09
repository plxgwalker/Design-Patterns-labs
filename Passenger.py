from Ticket import Ticket
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
