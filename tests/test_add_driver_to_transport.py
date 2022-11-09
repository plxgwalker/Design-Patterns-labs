import Transport
import Driver
from unittest import TestCase


test_driver = Driver
test_driver.driver_info = (0, "sad", "sadfs", 23, 2)
test_train = Transport.Train()


class TestAddDriverToTransport(TestCase):
    def test_add_driver(self):
        actual = test_train.add_driver(test_driver)
        expected = f"Added driver with ID: 0."
        self.assertEqual(actual, expected)
