import random

from test.bankApp.account import *


class Bank:

    def __init__(self, bank_name):

        self.bank_name = bank_name
        self.account_info = []
        self.account_detail = []

    def register(self, firstName, lastName, pin):

        new_account = Account(self.generate_account_Number(), f"{firstName} {lastName}", pin)
        self.account_info.append(new_account)

    @staticmethod
    def generate_account_Number():
        account_number = "23" + f"{random.randint(100000000, 990000000)}"

        return account_number

    def number_of_accounts(self):
        return len(self.account_info)

    def find_account(self, accountNumber) -> str:
        for account in self.account_info:
            if account.get_account_number() == accountNumber:
                return account

        raise TypeError("Account number not found")

    def check_balance(self, account_number, pin):
        return self.find_account(account_number).check_Balance(pin)

    def deposit(self, account_number, amount):
        return self.find_account(account_number).deposit(amount)

    def withdraw(self, account_number, amount, pin):
        return self.find_account(account_number).withdraw(amount, pin)

    def transfer(self, sender_account_number, receiver_account_number, amount, pin):

        self.find_account(sender_account_number).withdraw(amount, pin)
        self.find_account(receiver_account_number).deposit(amount)

    def add_new_user(self, user_name, password):
        new_account_login = Account(user_name, password)
        self.account_detail.append(new_account_login)
