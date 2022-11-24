from dataclasses import dataclass
from abc import ABC, abstractmethod


@dataclass
class TransportInfo:
    """Represents dataclass of information about 'Transport'.

    Arguments:
        id (int): ID of 'Transport'.
        passengers_limit (int): Limit of passengers in 'Transport'.
        weight_limit (int): Limit of tons in 'Transport'.

    """
    id: int
    passengers_limit: int
    weight_limit: float


class Transport(ABC):
    """Represents class 'Transport'.

    Properties:
        @property
        transport_info ():
            Returns parameter '_transport_info'.

        @transport_info.setter
        transport_info (transport_info: TransportInfo):
            Setting parameter '_transport_info' values of 'transport_info'.

    Methods:
        @abstractmethod
        add_driver (driver) -> str:
            Setting parameter 'driver' values of 'driver'.

        @abstractmethod
        add_type_of_transport (transport_type: str) -> str:
            Setting parameter 'transport_type' values of 'transport_type'.

    Returns:
        add_driver (driver) -> str:
            String of commit.

        add_type_of_transport (transport_type: str) -> str:
            String of commit.

    """
    def __init__(self):
        self._transport_info = None
        self.driver = None
        self.type = None

    @property
    def transport_info(self):
        return self._transport_info

    @transport_info.setter
    def transport_info(self, transport_info: TransportInfo):
        if isinstance(transport_info, TransportInfo):
            self._transport_info = transport_info

    @abstractmethod
    def add_driver(self, driver) -> str:
        self.driver = driver
        return f"Added driver for transport {self.transport_info.id}."

    @abstractmethod
    def add_type_of_transport(self, transport_type: str) -> str:
        self.type = transport_type
        return f"Added type of transport."


class Train(Transport):
    """Represents class 'Train' which inherits class 'Transport'.

    Methods:
        add_driver (driver) -> str:
            Setting parameter 'driver' values of 'driver'.

        add_type_of_transport (transport_type: str) -> str:
            Setting parameter 'transport_type' values of 'transport_type' by default its 'Train'.

    Returns:
        add_driver (driver) -> str:
            String of commit.

        add_type_of_transport (transport_type: str) -> str:
            String of commit.

    """
    def add_driver(self, driver) -> str:
        self.driver = driver
        return f"Added driver with ID: {self.driver.driver_info[0]}."

    def add_type_of_transport(self, transport_type: str = "Train") -> str:
        self.type = transport_type
        return f"Added transport type: {self.type}."


class Bus(Transport):
    """Represents class 'Bus' which inherits class 'Transport'.

    Methods:
        add_driver (driver) -> str:
            Setting parameter 'driver' values of 'driver'.

        add_type_of_transport (transport_type: str) -> str:
            Setting parameter 'transport_type' values of 'transport_type' by default its 'Bus'.

    Returns:
        add_driver (driver) -> str:
            String of commit.

        add_type_of_transport (transport_type: str) -> str:
            String of commit.

    """
    def add_driver(self, driver) -> str:
        self.driver = driver
        return f"Added driver with ID: {self.driver.driver_info[0]}."

    def add_type_of_transport(self, transport_type: str = "Bus") -> str:
        self.type = transport_type
        return f"Added transport type: {self.type}."


class Truck(Transport):
    """Represents class 'Truck' which inherits class 'Transport'.

    Methods:
        add_driver (driver) -> str:
            Setting parameter 'driver' values of 'driver'.

        add_type_of_transport (transport_type: str) -> str:
            Setting parameter 'transport_type' values of 'transport_type' by default its 'Truck'.

    Returns:
        add_driver (driver) -> str:
            String of commit.

        add_type_of_transport (transport_type: str) -> str:
            String of commit.

    """
    def add_driver(self, driver) -> str:
        self.driver = driver
        return f"Added driver with ID: {self.driver.driver_info[0]}."

    def add_type_of_transport(self, transport_type: str = "Truck") -> str:
        self.type = transport_type
        return f"Added transport type: {self.type}."
