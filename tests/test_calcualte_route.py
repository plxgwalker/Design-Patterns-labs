import Route
from Ticket import Ticket, TicketInfo
from unittest import TestCase


test_ticket = Ticket()
test_ticket_info = TicketInfo(0, "Lviv", "Kyiv", "Truck")
test_ticket.ticket_info = test_ticket_info

route_lviv_kyiv = Route.Route("Lviv", "Kyiv")


class TestRouteCalculation(TestCase):
    def test_route_calculation(self):
        actual = route_lviv_kyiv.route_info(test_ticket)
        expected = print(f"Distance: 632.9 km.\nTime in minutes: 622.4.\nTime in hours: 10.4.\nTime in day/s: 0.4.")
        self.assertEqual(actual, expected)
