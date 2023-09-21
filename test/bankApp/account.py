from test.bankApp.exception import *


class Account:

    def __init__(self, accountNumber, accountName, pin):
        self.accountNumber = accountNumber
        self.accountName = accountName
        self.PIN = pin
        self.balance = 0

    @staticmethod
    def validate_digit_type(amount):
        if type(amount) not in [int, float]:
            raise EntryError("invalid entry")

    def validatePin(self, pin):
        if self.PIN != pin:
            raise PinError("Incorrect pin")

    def validate_amount(self, amount):
        if amount < 0:
            raise AmountLessThanZero("Amount can't be less than zero")

        elif amount > self.balance:

            raise AmountIsGreaterThanBalance("insufficient fund")

    def check_Balance(self, pin) -> int:
        self.validatePin(pin)

        return self.balance

    def deposit(self, amount) -> int or float:
        self.validate_digit_type(amount)

        if amount > 0:
            self.balance += amount

    def withdraw(self, amount, pin) -> int or float:
        self.validatePin(pin)
        self.validate_digit_type(amount)
        self.validate_amount(amount)
        self.balance -= amount

    def updatePin(self, pin, enter_new_Pin):
        self.validatePin(pin)

        self.PIN = enter_new_Pin

    def get_account_number(self) -> str:
        return self.accountNumber

    def get_account(self) -> str:

        return f"{self.accountNumber} {self.accountName} {self.PIN}"
