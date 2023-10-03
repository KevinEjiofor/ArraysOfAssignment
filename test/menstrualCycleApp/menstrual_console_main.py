import tkinter as tk
from tkinter import simpledialog, messagebox
from datetime import datetime

from test.menstrualCycleApp.mentrual import MenstrualCycle


class MenstrualApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Menstrual Cycle Tracking App")
        self.cycles = MenstrualCycle()
        self.user_name = ""

    def run(self):
        self.welcome_page()

    def get_input(self, prompt):
        return simpledialog.askstring("Input", prompt, parent=self.root)

    def display_message(self, message):
        messagebox.showinfo("Information", message)

    def welcome_page(self):
        try:
            login = self.get_input("Enter:\n\n1-> Menu page\n2-> Exit App\n\n")
            if login is not None and login.strip() != "":
                choice = login.strip()[0]
                if choice == '1':
                    self.create_an_account()
                elif choice == '2':
                    self.exit_app()
                else:
                    raise ValueError("Invalid input. Please enter '1' or '2'.")
            else:
                raise ValueError("Invalid input. Please enter '1' or '2'.")

        except ValueError as e:
            self.display_message(str(e))
            self.welcome_page()

    def exit_app(self):
        try:
            user = self.get_input("Do you want to EXIT the app? Enter Yes/No: ").strip().lower()

            if user == "yes":
                self.display_message("Bye!")
                self.root.destroy()
            elif user == "no":
                self.welcome_page()
            else:
                raise ValueError("Invalid input. Please enter 'yes' or 'no'.")

        except ValueError as e:
            self.display_message(str(e))
            self.exit_app()

    def create_an_account(self):
        try:
            user = self.get_input("What name do you want to be called: ").strip()
            if not user.isalpha():
                raise ValueError("Invalid entry. Name should only contain letters.")

            self.user_name = user

            year_of_birth = self.get_input("Kindly enter your year of birth: ").strip()
            if not year_of_birth.isdigit() or len(year_of_birth) != 4:
                raise ValueError("Invalid year of birth. Please enter a 4-digit year.")

            self.menu_page()

        except ValueError as e:
            self.display_message(str(e))
            self.welcome_page()

    def menu_page(self):
        try:
            self.display_message(
                f"Hello {self.user_name}!\n\n"
                "Welcome to our menstrual cycle tracking app! We're here to help you gain valuable insights into your menstrual cycle and ovulation patterns.\n\n"
                "It's important to remember that while our app provides valuable information and predictions, no method of tracking or predicting your cycle is foolproof and can guarantee 100% accuracy.\n\n"
                "The human body is complex, and menstrual cycles can vary from person to person and even from month to month.\n\n"
                "Our app uses data and algorithms to make predictions based on patterns, but there can be natural variations and unexpected factors that influence your cycle.\n\n"
                "We encourage you to use this app as a helpful tool for understanding your body and planning various aspects of your life, such as fertility, period dates, and more. However, always consult with healthcare professionals for important decisions related to your health and family planning.\n\n"
                "Remember, our goal is to empower you with knowledge and insights, but your health and well-being are of utmost importance.\n\n"
                "Use this app as a valuable resource, but make informed decisions based on your unique circumstances.\n\n"
                "Thank you for choosing our app, and we're here to support you on your journey of self-awareness and health management."
            )

            menu = self.get_input(
                "Enter:\n\n1-> Cycle Status\n2-> Next Menstrual Period\n3-> Ovulation Period\n4-> Period Status\n5-> Home Page\n"
            ).strip()

            if menu is not None and menu.strip() != "":
                choice = menu.strip()[0]
                if choice == '1':
                    self.cycles_status()
                elif choice == '2':
                    self.next_menstrual()
                elif choice == '3':
                    self.ovulation_period()
                elif choice == '4':
                    self.period_status()
                elif choice == '5':
                    self.welcome_page()
                else:
                    raise ValueError("Invalid input. Please enter '1' through '5'.")
            else:
                raise ValueError("Invalid input. Please enter '1' through '5'.")

        except ValueError as e:
            self.display_message(str(e))
            self.menu_page()

    def back_to_home(self):
        self.welcome_page()

    def period_status(self):
        try:
            start_menstruation_str = self.get_input("When did you start menstruation (yyyy-MM-dd): ").strip()
            end_menstruation_str = self.get_input("When did you stop your menstruation (yyyy-MM-dd): ").strip()

            start_menstruation = datetime.strptime(start_menstruation_str, "%Y-%m-%d").date()
            end_menstruation = datetime.strptime(end_menstruation_str, "%Y-%m-%d").date()

            status = self.cycles.period_length_status(start_menstruation, end_menstruation)
            self.display_message(f"Period status: {status}")

        except (ValueError, TypeError) as e:
            self.display_message("Invalid date format. Please enter the date in yyyy-MM-dd format.")
            self.menu_page()

    def ovulation_period(self):
        try:
            self.display_message(
                "The menstrual cycle refers to several hormonal changes that occur as a female's body prepares for pregnancy.\n"
                "A full menstrual cycle begins on the first day of a period and ends the day before the next period."
            )

            start_menstruation_str = self.get_input("When did you start menstruation (yyyy-MM-dd): ").strip()
            end_menstruation_str = self.get_input("When did you stop your menstruation (yyyy-MM-dd): ").strip()

            start_menstruation = datetime.strptime(start_menstruation_str, "%Y-%m-%d").date()
            end_menstruation = datetime.strptime(end_menstruation_str, "%Y-%m-%d").date()

            self.cycles.set_start_menstruation(start_menstruation)
            self.cycles.set_end_menstruation(end_menstruation)

            self.display_message(
                "What is cycle length?\n"
                "The menstrual cycle is counted from the first day of one period to the first day of the next.\n"
                "The cycle isn't the same for everyone. Menstrual bleeding might happen every 21 to 35 days and last 2 to 7 days.\n"
                "For the first few years after menstruation begins, long cycles are common."
            )

            cycle = self.get_input("Kindly enter your last cycle length: ").strip()
            self.cycles.set_cycle_length(int(cycle))

            self.display_message(f"{self.user_name}, your ovulation period is from: {self.cycles.calculate_ovulation_period()}")

        except (ValueError, TypeError) as e:
            self.display_message("Invalid date format. Please enter the date in yyyy-MM-dd format.")
            self.menu_page()

    def next_menstrual(self):
        try:
            self.display_message(
                "The menstrual cycle refers to several hormonal changes that occur as a female's body prepares for pregnancy.\n"
                "A full menstrual cycle begins on the first day of a period and ends the day before the next period."
            )

            start_menstruation_last = self.get_input("When did you start your last menstruation (yyyy-MM-dd): ").strip()
            end_menstruation_last = self.get_input("When did your last menstruation stop (yyyy-MM-dd): ").strip()

            start_menstruation = datetime.strptime(start_menstruation_last, "%Y-%m-%d").date()
            end_menstruation = datetime.strptime(end_menstruation_last, "%Y-%m-%d").date()

            self.cycles.set_start_menstruation(start_menstruation)
            self.cycles.set_end_menstruation(end_menstruation)

            result = self.cycles.calculate_next_cycle()
            self.display_message(f"{self.user_name}, your next menstruation should be on: {result}")
            self.menu_page()

        except (ValueError, TypeError) as e:
            self.display_message("Invalid date format. Please enter the date in yyyy-MM-dd format.")
            self.menu_page()

    def cycles_status(self):
        try:
            self.display_message(
                "What is cycle length?\n"
                "The menstrual cycle is counted from the first day of one period to the first day of the next.\n"
                "The cycle isn't the same for everyone. Menstrual bleeding might happen every 21 to 35 days and last 2 to 7 days.\n"
                "For the first few years after menstruation begins, long cycles are common."
            )

            cycle = self.get_input("Kindly enter your cycle length: ").strip()
            self.cycles.set_cycle_length(int(cycle))
            status = self.cycles.cycle_length_status()
            self.display_message(f"{self.user_name}, your cycle length is {status}")
            self.menu_page()

        except (ValueError, TypeError) as e:
            self.display_message("Invalid input. Please enter a valid number.")
            self.menu_page()

if __name__ == "__main__":
    app = MenstrualApp()
    app.run()
