from code import Route
from code.Ticket import Ticket, TicketInfo
from unittest import TestCase
# redo test

test_ticket = Ticket()
test_ticket_info = TicketInfo(0, "Lviv", "Kyiv", "Truck")
test_ticket.ticket_info = test_ticket_info

route_lviv_kyiv = Route.Route("Lviv", "Kyiv")


class TestRouteCalculation(TestCase):
    def test_route_calculation(self):
        actual = route_lviv_kyiv.route_info(test_ticket)
        expected = [632.9, 10.4, "Lviv", "Kyiv"]
        self.assertEqual(actual, expected)
