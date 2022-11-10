from Depo import Depo, DepoInfo
from Passenger import Passenger, PassengerInfo
from unittest import TestCase


test_passenger = Passenger()
test_depo = Depo()
test_passenger.passenger_info = PassengerInfo(0, "Test", "test", 20, [])
test_depo.depo_info = DepoInfo(0, "Lviv", [], [], [], [])

test_depo.create_tickets("Kyiv", 3, "Train")


class TestBuyTicket(TestCase):
    def test_buy_ticket(self):
        test_depo.buy_ticket(test_passenger)
        actual = test_passenger.passenger_info.tickets
        expected = [2]
        self.assertEqual(actual, expected)
