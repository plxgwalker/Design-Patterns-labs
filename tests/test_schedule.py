from unittest import TestCase
from code.Schedule import Schedule
from code.Depo import Depo, DepoInfo
import datetime

test_depo = Depo()
test_depo_info = DepoInfo(1, "Lviv", [], [], [], [])
test_depo.depo_info = test_depo_info
test_depo.create_tickets("Kyiv", 2, "Bus")

test_schedule = Schedule(test_depo.depo_info.tickets)
test_schedule.create_schedule()


class TestSchedule(TestCase):
    def test_schedule(self):
        actual = test_schedule.schedule
        print(test_schedule.schedule)
        now = datetime.datetime.now().replace(second=0, microsecond=0)
        expected = f"Schedule:\n" \
                   f"\nDeparture: {now} Arrive: {now + datetime.timedelta(hours=10.4)} Lviv -> Kyiv Distance: 632.9" \
                   f"\nDeparture: {now} Arrive: {now + datetime.timedelta(hours=10.4)} Lviv -> Kyiv Distance: 632.9"
        self.assertEqual(actual, expected)
