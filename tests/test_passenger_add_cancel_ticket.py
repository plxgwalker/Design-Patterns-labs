from unittest import TestCase
from code.Passenger import PassengerInfo, Passenger
from code.Ticket import TicketInfo, Ticket


test_ticket = Ticket()
test_ticket_info = TicketInfo(0, "Lviv", "Kyiv", "Train")
test_ticket.ticket_info = test_ticket_info

test_passenger = Passenger()
test_passenger_info = PassengerInfo(0, "Test", "Passenger", 30, [])
test_passenger.passenger_info = test_passenger_info


class TestTicket(TestCase):
    def test_add_ticket(self):
        test_passenger.add_ticket(test_ticket)
        actual = test_passenger.passenger_info.tickets
        expected = [0]
        self.assertEqual(actual, expected)

    def test_cancel_ticket(self):
        test_passenger.cancel_ticket(test_ticket)
        actual = test_passenger.passenger_info.tickets
        expected = []
        self.assertEqual(actual, expected)
