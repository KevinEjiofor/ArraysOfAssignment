import unittest
from datetime import datetime, timedelta

from test.menstrualCycleApp.mentrual import MenstrualCycle


class TestMenstrualCycle(unittest.TestCase):
    def setUp(self):
        self.cycle = MenstrualCycle()

    def test_set_cycle_length(self):
        self.cycle.set_cycle_length(28)
        self.assertEqual(self.cycle.cycle_length, 28)

        with self.assertRaises(ValueError):
            self.cycle.set_cycle_length(0)

    def test_cycle_length_status(self):
        self.cycle.set_cycle_length(28)
        self.assertEqual(self.cycle.cycle_length_status(), "Normal")

        with self.assertRaises(ValueError):
            self.cycle.set_cycle_length(15)
            self.cycle.cycle_length_status()

    def test_cycle_length_status_high(self):
        self.cycle.set_cycle_length(28)
        self.assertEqual(self.cycle.cycle_length_status(), "Normal")

        self.cycle.set_cycle_length(15)

        self.assertRaises(ValueError, self.cycle.cycle_length_status)

    def test_set_start_and_end_menstruation(self):
        start_date = datetime(2023, 11, 2)
        end_date = datetime(2023, 11, 7)

        self.cycle.set_start_menstruation(start_date)
        self.cycle.set_end_menstruation(end_date)

        self.assertEqual(self.cycle.start_menstruation, start_date)
        self.assertEqual(self.cycle.end_menstruation, end_date)

    def test_calculate_ovulation_period(self):
        start_menstruation = datetime(2023, 11, 2)
        end_menstruation = datetime(2023, 11, 7)
        self.cycle.set_start_menstruation(start_menstruation)
        self.cycle.set_end_menstruation(end_menstruation)

        self.cycle.set_cycle_length(28)

        ovulation_period = self.cycle.calculate_ovulation_period()

        expected_ovulation_period = "Nov 14, 2023 - Nov 18, 2023"

        self.assertEqual(expected_ovulation_period, ovulation_period)

    def test_calculate_next_cycle(self):
        start_menstruation = datetime(2023, 11, 2)
        end_menstruation = datetime(2023, 11, 7)
        self.cycle.set_start_menstruation(start_menstruation)
        self.cycle.set_end_menstruation(end_menstruation)

        self.cycle.set_cycle_length(28)

        calculate_next_cycle = self.cycle.calculate_next_cycle()

        expected_menstruation_date_to_start = "Dec 05, 2023"

        self.assertEqual(expected_menstruation_date_to_start, calculate_next_cycle)

    def test_period_length_status(self):
        start_menstruation = datetime(2023, 11, 2)
        end_menstruation = datetime(2023, 11, 7)

        status = self.cycle.period_length_status(start_menstruation, end_menstruation)

        self.assertEqual("Normal", status)

    def test_period_length(self):
        start_menstruation = datetime(2023, 11, 2)
        end_menstruation = datetime(2023, 11, 12)

        with self.assertRaises(ValueError):
            self.cycle.period_length_status(start_menstruation, end_menstruation)

    def test_period_length_for_zero_condition(self):
        start_menstruation = datetime(2023, 11, 2)
        end_menstruation = datetime(2023, 11, 2)

        self.assertRaises(ValueError, self.cycle.period_length_status, start_menstruation, end_menstruation)
