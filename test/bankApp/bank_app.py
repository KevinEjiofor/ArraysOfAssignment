import re
from test.bankApp.bank import Bank
from test.bankApp.exception import *


class BankApp:
    bank = Bank("Access_bank")

    def __init__(self):
        self.user_name = " "
        self.main_password = " "

    @staticmethod
    def welcome_page():
        try:
            welcome_display = BankApp.input_method(
                """
                WELCOME TO ZIGGY XCHANGE
                Enter:
                1-> Register Account

                2-> Log in

                3-> Exit
                """)
            if welcome_display:
                choice = welcome_display[0]
                if choice == "1":
                    BankApp.bank_registration()

                elif choice == "2":
                    BankApp.bank_log_in()

                elif choice == "3":
                    BankApp.exit()

                else:
                    raise ValueError("Invalid input. Please enter '1 - 3' to create a diary account.")
            else:
                raise ValueError("Invalid input. Please enter '1 - 3' to create a diary account.")
        except CustomerException as error:
            BankApp.display_method(str(error))
            BankApp.welcome_page()

    @staticmethod
    def bank_registration():
        try:

            user_name = BankApp.input_method("Kindly enter your first name: ")
            BankApp.validate_name_input(user_name)

            surname = BankApp.input_method("Kindly enter your last name: ")
            BankApp.validate_name_input(surname)

            password = BankApp.input_method("Enter a password: ")
            BankApp.password(password)

            payment = BankApp.input_method("Enter payment: ")
            BankApp.pin(payment)

            account_number = BankApp.bank.generate_account_Number()
            BankApp.bank.register(user_name, surname, payment)
            BankApp.display_method(f"""
                        {"=" * 50}
                          Account Name: {user_name} {surname}
                          
                          Account User name: {user_name}{surname}
                          
                          Account Number: {account_number}
                          
                          Account created successfully!
                            
                             BASE ON BELIEVE
                        {"=" * 50}
                                """)

            BankApp.user_name = f"{user_name}{surname}"
            BankApp.main_password = password

            BankApp.bank_log_in()

        except CustomerException as error:
            BankApp.display_method(str(error))
            BankApp.bank_registration()

    @staticmethod
    def input_method(prompt):
        return input(prompt)

    @staticmethod
    def display_method(prompt):
        print(prompt)

    @staticmethod
    def password(pin):
        pattern = r"^\d{6}$"
        if not re.search(pattern, pin):
            raise CustomerException("Password should be in six digits ")

    @staticmethod
    def pin(pin):
        pattern = r"^\d{4}$"

        if not re.search(pattern, pin):
            raise CustomerException("Payment pin should be in four digits")

    @staticmethod
    def validate_name_input(full_name):
        pattern = r"^\D*$"
        if not re.fullmatch(pattern, full_name):
            raise CustomerException("Invalid name")

    @classmethod
    def bank_log_in(cls):
        pass

    @classmethod
    def exit(cls):
        try:
            user = BankApp.input_method("\nDo you want to EXIT the diary? Enter Yes/No: ").casefold()
            if user == "yes":
                BankApp.display_method("Bye! "
                                       "Thank you ")

            elif user == "no":
                BankApp.welcome_page()
            else:
                raise ValueError("\nInvalid input. Please enter 'YES' or 'NO'.")

        except ValueError as error:
            BankApp.display_method(str(error))
            BankApp.exit()


if __name__ == '__main__':
    caller = BankApp()
    caller.welcome_page()
