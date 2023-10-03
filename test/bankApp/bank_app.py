import re
from test.bankApp.bank import Bank
from test.bankApp.exception import *


class BankApp:
    bank = Bank("Access_bank")

    @classmethod
    def welcome_page(cls):

        try:
            welcome_display = BankApp.input_method(
                f"""
            ==============================================================================
                                    WELCOME TO ZIGGY XCHANGE
            ===============================================================================   
                Enter:
                             1-> Register Account

                             2-> Transaction section

                             3-> Exit
                              
                              """)

            choice = welcome_display if welcome_display else " "

            if choice == "1":
                BankApp.bank_registration()

            elif choice == "2":
                BankApp.bank_transaction()

            elif choice == "3":
                BankApp.exit()

            else:
                raise CustomerException("Invalid input. Please enter '1 - 3' to create a diary account.")

        except CustomerException as error:
            BankApp.display_method(str(error))
            BankApp.welcome_page()

    @classmethod
    def bank_registration(cls):
        try:

            user_name = BankApp.input_method("Kindly enter your first name: ")
            BankApp.validate_name_input(user_name)

            surname = BankApp.input_method("Kindly enter your last name: ")
            BankApp.validate_name_input(surname)

            payment = BankApp.input_method("Enter payment pin(Four digit pin): ")
            BankApp.pin(payment)

            account_number = BankApp.bank.register(user_name, surname, payment)
            BankApp.display_method(f"""
                        {"=" * 80}
                        
                                 Account Name: {user_name} {surname}
                          
                                 Account Number: {account_number}
                          
                                     Account created successfully!
                            
                                             BASE ON BELIEVE 
                        {"=" * 80}
                                """)

            BankApp.user_name = f"{user_name}{surname}"
            BankApp.welcome_page()

        except (TypeError, AmountLessThanZero, AmountLessThanZero, CustomerException) as error:
            BankApp.display_method(str(error))
            BankApp.bank_registration()

    @classmethod
    def exit(cls):
        try:
            user = BankApp.input_method("\nDo you want to EXIT Ziggy App? Enter Yes/No: ").casefold()
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

    @classmethod
    def bank_transaction(cls):
        try:
            menu = BankApp.input_method(f"""
             
                 {"=" * 50}
                            ZIGGY XCHANGE     
                {"=" * 50}
                 
                 Enter:
            
                             1-> Balance
                            
                             2-> Deposit
                        
                             3-> Withdraw
                        
                             4-> Transfer
                             
                             5-> Home Page
                           
                        
                        """)
            choice = menu if menu else " "

            if choice == '1':
                BankApp.balance()

            elif choice == "2":
                BankApp.deposit()

            elif choice == "3":
                BankApp.withdraw()

            elif choice == "4":
                BankApp.transfer()

            elif choice == "5":
                BankApp.welcome_page()

            else:
                raise CustomerException("Invalid input. Please select a valid option (1-5).")

        except (TypeError, AmountLessThanZero, AmountLessThanZero, CustomerException) as error:
            BankApp.display_method(str(error))
            BankApp.bank_transaction()

    @classmethod
    def balance(cls):
        try:
            account_number = BankApp.input_method("Enter account number:  ")
            BankApp.validate_number_input(account_number)

            pin = BankApp.input_method("Enter pin: ")
            BankApp.pin(pin)

            getbalance = BankApp.bank.check_balance(account_number, pin)

            BankApp.display_method(F""""
                             {"+" * 20}
                                       
                                BALANCE:
                                                 
                                        {getbalance}
                             
                             {"+" * 20}
                                   """)
            BankApp.bank_transaction()

        except (TypeError, AmountLessThanZero, AmountLessThanZero, CustomerException) as error:
            BankApp.display_method(str(error))
            BankApp.bank_transaction()

    @classmethod
    def withdraw(cls):
        try:
            account_number = BankApp.input_method("Enter account number:  ")
            BankApp.validate_number_input(account_number)

            amount = BankApp.input_method("Enter amount:  ")
            BankApp.validate_number_input(amount)

            pin = BankApp.input_method("Enter pin: ")
            BankApp.pin(pin)

            BankApp.bank.withdraw(account_number, int(amount), pin)

            BankApp.display_method(f"""Your withdrawal of {amount}
                                            was successful""")
            BankApp.bank_transaction()

        except (TypeError, AmountLessThanZero, AmountLessThanZero, CustomerException) as error:
            BankApp.display_method(str(error))
            BankApp.bank_transaction()

    @classmethod
    def transfer(cls):
        try:
            sender_account_number = BankApp.input_method("Enter sender account number:  ")
            BankApp.validate_number_input(sender_account_number)

            receiver_account_number = BankApp.input_method("Enter receiver account number:  ")
            BankApp.validate_number_input(sender_account_number)

            amount = BankApp.input_method("Enter amount:  ")
            BankApp.validate_number_input(amount)

            pin = BankApp.input_method("Enter pin: ")
            BankApp.pin(pin)

            BankApp.bank.transfer(sender_account_number, receiver_account_number, int(amount), pin)
            BankApp.bank_transaction()

        except (TypeError, AmountLessThanZero, AmountLessThanZero, CustomerException) as error:
            BankApp.display_method(str(error))
            BankApp.bank_transaction()

    @classmethod
    def deposit(cls):
        try:
            account_number = BankApp.input_method("Enter account number:  ")
            BankApp.validate_number_input(account_number)

            amount = BankApp.input_method("Enter amount:  ")
            BankApp.validate_number_input(amount)

            BankApp.bank.deposit(account_number, int(amount))
            BankApp.display_method("Your transaction was successful")
            BankApp.bank_transaction()

        except (TypeError, AmountLessThanZero, AmountLessThanZero, CustomerException) as error:
            BankApp.display_method(str(error))
            BankApp.bank_transaction()

    @staticmethod
    def input_method(prompt):
        return input(prompt)

    @staticmethod
    def display_method(prompt):
        print(prompt)

    @staticmethod
    def pin(pin):
        pattern = r"^\d{4}$"

        if not re.search(pattern, pin):
            raise CustomerException("Payment pin should be in four digits")

    @staticmethod
    def validate_name_input(full_name):
        pattern = r"^\D*$"
        if not re.fullmatch(pattern, full_name):
            raise CustomerException("Invalid entry")

    @staticmethod
    def validate_number_input(number):
        pattern = r"^\d*$"
        if not re.fullmatch(pattern, number):
            raise CustomerException("Invalid entry")


if __name__ == '__main__':
    caller = BankApp()
    caller.welcome_page()
