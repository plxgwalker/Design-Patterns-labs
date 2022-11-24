from code.Depo import Depo, DepoInfo
from unittest import TestCase


LvivDepo = Depo()
LvivDepo_info = DepoInfo(0, "Lviv", [], [], [], [])
LvivDepo.depo_info = LvivDepo_info


class TestDepoFunctions(TestCase):
    def test_create_new_tickets(self):
        actual = LvivDepo.create_tickets("Kyiv", 1, "Train")
        expected = f"Added tickets:\nAmount of tickets: 1\nFrom: Lviv to Kyiv\nTransport type: Train"
        self.assertEqual(actual, expected)

    def test_print_all_tickets(self):
        actual = f"{LvivDepo.print_all_tickets()}"
        expected = f"TicketInfo(id=0, start_point='Lviv', finish_point='Kyiv', transport_type='Train')\n"
        self.assertEqual(actual, expected)
