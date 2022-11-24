from code import Transport, Driver
from unittest import TestCase


test_driver = Driver
test_train = Transport.Train()


class TestAddDriverToTransport(TestCase):
    def test_add_driver(self):
        actual = test_train.add_type_of_transport()
        expected = f"Added transport type: Train."
        self.assertEqual(actual, expected)

