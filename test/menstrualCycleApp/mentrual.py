from datetime import datetime, timedelta


class MenstrualCycle:
    def __init__(self):
        self.user_name = ""
        self.input_password = ""
        self.start_menstruation = None
        self.end_menstruation = None
        self.cycle_length = 0
        self.cycle_status = ""

    def register(self, user_name, input_password):
        self.user_name = user_name
        self.input_password = input_password

    def set_cycle_length(self, days):
        if days <= 0:
            raise ValueError("Invalid cycle length. Please set a positive value for cycle length.")
        self.cycle_length = days
        self.cycle_status = ""

    def cycle_length_status(self):
        if 21 <= self.cycle_length <= 35:
            self.cycle_status = "NORMAL"
        else:
            raise ValueError("This is NOT NORMAL. Kindly consult a doctor.")
        return self.cycle_status

    def set_start_menstruation(self, start_menstruation):
        self.start_menstruation = start_menstruation

    def set_end_menstruation(self, end_menstruation):
        self.end_menstruation = end_menstruation

    def calculate_ovulation_period(self):
        if self.start_menstruation is None:
            raise ValueError("Start menstruation date is not set.")

        half_of_cycle = self.cycle_length // 2
        ovulation_date = self.start_menstruation + timedelta(days=half_of_cycle)
        start_ovulation_period = ovulation_date - timedelta(days=2)
        end_ovulation_period = ovulation_date + timedelta(days=2)

        return f"{start_ovulation_period.strftime('%b %d, %Y')} - {end_ovulation_period.strftime('%b %d, %Y')}"

    def calculate_next_cycle(self):
        if self.end_menstruation is None:
            raise ValueError("End menstruation date is not set.")

        next_cycle_start = self.end_menstruation + timedelta(days=self.cycle_length)
        return next_cycle_start.strftime('%b %d, %Y')

    @staticmethod
    def period_length_status(start_menstruation, end_menstruation):
        if start_menstruation is None or end_menstruation is None:
            raise ValueError("Start and end menstruation dates are not set.")

        period_length = (end_menstruation - start_menstruation).days

        if period_length <= 0 or period_length > 7:
            raise ValueError("This is NOT NORMAL. Kindly consult a doctor.")
        else:
            return "NORMAL"

