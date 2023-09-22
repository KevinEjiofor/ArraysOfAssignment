import re

from diaries import Diaries, CustomerException


class DiaryBook:
    diaries = Diaries()

    def __init__(self):
        self.user_name = ""
        self.password = ""

    @staticmethod
    def display_welcome_page():
        try:
            welcome_page = DiaryBook.input_method("""
                WELCOME
                LEAVING YOUR IMPACT FOR ETERNITY (LIFE)

                1. Create a diary account
                
                2. Log in
                
                3. Exit
                """)

            if welcome_page:
                choice = welcome_page[0]
                if choice == '1':
                    DiaryBook.diary_user_register()
                elif choice == '2':
                    DiaryBook.login()
                elif choice == '3':
                    DiaryBook.exit_menu()
                else:
                    raise ValueError("Invalid input. Please enter '1 - 3' to create a diary account.")
            else:
                raise ValueError("Invalid input. Please enter '1 - 3' to create a diary account.")

        except (ValueError, CustomerException) as error:
            DiaryBook.display_method(str(error))
            DiaryBook.display_welcome_page()

    @staticmethod
    def exit_menu():
        try:
            user = DiaryBook.input_method("\nDo you want to EXIT the diary? Enter Yes/No: ").casefold()
            if user == "yes":
                DiaryBook.display_method("Bye!")
            elif user == "no":
                DiaryBook.display_welcome_page()
            else:
                raise ValueError("\nInvalid input. Please enter 'YES' or 'NO'.")

        except ValueError as error:
            DiaryBook.display_method(str(error))
            DiaryBook.exit_menu()

    @staticmethod
    def login():
        try:
            user = DiaryBook.input_method("Enter user name: ")
            user_password = DiaryBook.input_method("Enter password: ")
            DiaryBook.user_name = user
            DiaryBook.password = user_password
            DiaryBook.diaries.find_user(user).unlock(user_password)
            DiaryBook.main_menu()

        except Exception as error:
            DiaryBook.display_method(str(error))
            DiaryBook.display_welcome_page()

    @staticmethod
    def diary_user_register():
        try:
            user_name = DiaryBook.input_method("Kindly enter your name: ")
            DiaryBook.validate_name_input(user_name)

            password = DiaryBook.input_method("Enter a password: ")
            DiaryBook.password(password)

            if len(user_name) == 0 or len(password) == 0:

                raise ValueError("Username and password cannot be empty.")

            DiaryBook.diaries.add_new_user(user_name, password)

            DiaryBook.display_method("Diary created successfully!")
            DiaryBook.display_welcome_page()

        except ValueError as error:
            DiaryBook.display_method(str(error))

    @staticmethod
    def main_menu():
        try:
            menu = DiaryBook.input_method("""
                    1. Create entry
                    
                    2. Update entry
                    
                    3. Delete entry
                    
                    4. Search for entry
                    
                    5. Log out
                    """)
            choice = menu[0] if menu else ""

            if choice == '1':
                DiaryBook.create_entry()
            elif choice == '2':
                DiaryBook.update_entry()
            elif choice == '3':
                DiaryBook.delete_entry()
            elif choice == '4':
                DiaryBook.find_id()
            elif choice == '5':
                DiaryBook.logout()
            else:
                raise CustomerException("Invalid input. Please select a valid option (1-5).")

        except CustomerException as error:
            DiaryBook.display_method(str(error))

    @staticmethod
    def logout():
        DiaryBook.diaries.find_user(DiaryBook.user_name).lock_diary()
        DiaryBook.display_welcome_page()

    @staticmethod
    def find_id():
        try:
            diary_id = int(DiaryBook.input_method("Enter ID number: "))
            entry = None
            if diary_id != 0:
                entry = DiaryBook.diaries.find_user(DiaryBook.user_name).find_entry(diary_id)
            if entry:
                DiaryBook.display_method(f"Diary with ID {diary_id} found: {entry.get_title()}\n{entry.get_body()}")
            DiaryBook.main_menu()

        except (CustomerException, ValueError) as error:
            DiaryBook.display_method(str(error))
            DiaryBook.main_menu()

    @staticmethod
    def delete_entry():
        try:
            entry_id = int(DiaryBook.input_method("Enter ID: "))
            if entry_id != 0:
                DiaryBook.diaries.find_user(DiaryBook.user_name).delete_entry(entry_id)
                DiaryBook.display_method(f"Diary with ID {entry_id} has been deleted")
                DiaryBook.main_menu()
            else:
                raise CustomerException("User not found.")

        except CustomerException as error:
            DiaryBook.display_method(str(error))
            DiaryBook.delete_entry()

    @staticmethod
    def update_entry():
        try:
            entry_id = int(DiaryBook.input_method("Enter id: "))
            entry = DiaryBook.diaries.find_user(DiaryBook.user_name).find_entry(entry_id)
            DiaryBook.display_method(f"Diary with ID {entry_id} found: {entry.get_title()}\n{entry.get_body()}")
            title = DiaryBook.input_method("Update title: ")
            body = DiaryBook.input_method("Update body: ")
            DiaryBook.diaries.find_user(DiaryBook.user_name).update_entry(entry_id, title, body)
            DiaryBook.display_method("Entry updated successfully.")
            DiaryBook.main_menu()

        except CustomerException as error:
            DiaryBook.display_method(str(error))
            DiaryBook.main_menu()

    @staticmethod
    def password(pin):
        pattern = r"^\d{6}$"
        if not re.search(pattern, pin):
            raise CustomerException("Password should be in six digits ")

    @staticmethod
    def validate_name_input(full_name):
        pattern = r"^\D*$"
        if not re.fullmatch(pattern, full_name):
            raise CustomerException("Invalid name")

    @staticmethod
    def create_entry():
        try:
            title = DiaryBook.input_method("Title: ")
            body = DiaryBook.input_method("Body: ")

            if not title or not body:
                raise CustomerException("Title or body cannot be empty.")
            DiaryBook.diaries.find_user(DiaryBook.user_name).create_entry(title, body)
            DiaryBook.main_menu()

        except CustomerException as error:
            DiaryBook.display_method(str(error))

    @staticmethod
    def input_method(prompt):
        return input(prompt)

    @staticmethod
    def display_method(prompt):
        print(prompt)


if __name__ == "__main__":
    caller = DiaryBook()
    caller.display_welcome_page()
