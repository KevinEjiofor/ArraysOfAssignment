import unittest
from bank import *

from test.bankApp.bank import Bank
from test.bankApp.exception import *


class TestBankFunctions(unittest.TestCase):
    def setUp(self):
        self.bank = Bank("ziggy_bank")
        self.bank.register("Ziggy", "Gad", "pin")

    def test_to_register_more_than_one_account(self):
        self.bank.register("Joshua", "kompany", "8989")
        number_of_accounts = self.bank.number_of_accounts()
        self.assertEqual(2, number_of_accounts)

    def test_to_deposit(self):
        self.bank.deposit("1", 5_000)

        newAccountBalance = self.bank.check_balance("1", "pin")
        self.assertEquals(5000, newAccountBalance)

    def test_to_withdraw(self):
        self.bank.deposit("1", 10000)

        self.bank.withdraw("1", 5000, "pin")

        newAccountBalance = self.bank.check_balance("1", "pin")
        self.assertEquals(5000, newAccountBalance)

    def test_for_withdrawing_above_balance_amount(self):
        self.bank.deposit("1", 5000)

        currentBalance = self.bank.check_balance("1", "pin")
        self.assertEquals(5000, currentBalance)

        self.assertRaises(AmountIsGreaterThanBalance, self.bank.withdraw, "1", 10000, "pin")

    def test_for_negative_value_withdrawal(self):
        self.bank.deposit("1", 5000)

        currentBalance = self.bank.check_balance("1", "pin")
        self.assertEquals(5000, currentBalance)

        self.assertRaises(AmountLessThanZero, self.bank.withdraw, "1", -2000, "pin")

    def test_transfer(self):
        self.bank.deposit("1", 6000)

        self.bank.register("Joshua", "kompany", "8989")
        self.assertEquals(self.bank.find_account("2").get_account_number(),
                          Account("2", "Joshua kompany", "8989").get_account_number())

        self.bank.transfer("1", "2", 2000, "pin")

        newBalance = self.bank.check_balance("1", "pin")
        self.assertEquals(4000, newBalance)
        check_balance_of_the_second_account = self.bank.check_balance("2", "8989")
        self.assertEquals(2000, check_balance_of_the_second_account)
