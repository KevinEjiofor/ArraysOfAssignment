import unittest
from account import *



class TestAccountFunction(unittest.TestCase):
    def setUp(self):
        self.ziggyAccount = Account("0560946397","Ziggy", "8989")


    def test_we_can_deposit_Into_an_account(self):

        currentBalance = self.ziggyAccount.check_Balance("8989")
        self.assertEqual(0, currentBalance)

        self.ziggyAccount.deposit(5000)

        newBalance = self.ziggyAccount.check_Balance("8989")
        self.assertEqual(5000, newBalance)

    def test_deposit_twice(self):
        self.ziggyAccount.deposit(5000)

        currentBalance = self.ziggyAccount.check_Balance("8989")
        self.assertEqual(5000, currentBalance)

        self.ziggyAccount.deposit(2000)

        newBalance = self.ziggyAccount.check_Balance("8989")
        self.assertEqual(7000, newBalance)

    def test_we_cannot_deposit_negative_value(self):
        self.ziggyAccount.deposit(2000)

        currentBalance = self.ziggyAccount.check_Balance("8989")
        self.assertEqual(2000, currentBalance)

        self.ziggyAccount.deposit(-1000)

        newBalance = self.ziggyAccount.check_Balance("8989")
        self.assertEqual(2000, newBalance)

    def  test_withdrawal(self):

        self.ziggyAccount.deposit( 5000)
        currentAmount = self.ziggyAccount.check_Balance("8989")
        self.assertEqual(5000, currentAmount)

        self.ziggyAccount.withdraw(3000,"8989")

        newBalance = self.ziggyAccount.check_Balance("8989")
        self.assertEqual(2000, newBalance)

    def test_checking_balance_with_wrong_pin(self):

        self.ziggyAccount.deposit(5000)

        self.assertRaises(PinError,self.ziggyAccount.check_Balance,"8987")

    def  test_for_withdrawing_above_balance_amount(self):

        self.ziggyAccount.deposit(5000)

        currentBalance = self.ziggyAccount.check_Balance("8989")
        self.assertEqual(5000, currentBalance)

        self.assertRaises(AmountIsGreaterThanBalance,self.ziggyAccount.withdraw, 100000, "8989")





    def test_change_of_pin(self):

        self.ziggyAccount.updatePin("8989","9595")

        self.ziggyAccount.deposit(5000)

        newPinToCheckAccountBalance = self.ziggyAccount.check_Balance("9595")
        self.assertEquals(5000, newPinToCheckAccountBalance)











