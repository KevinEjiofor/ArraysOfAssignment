import re
import time
from colorama import Fore

def UserEntry():
    user = input(Fore.WHITE + "\nEnter password: ")

    Conditions(user)

def Conditions(user=None):

    if len(user) < 8:
        print(Fore.RED + "\nYour password is too short ")
        UserEntry()
        return False

    if not re.search("[A-Z]", user):
        print(Fore.RED +"\nkindly start with uppercase letters to your password ")
        UserEntry()
        return False

    if not re.search( "[a-z]", user):
        print(Fore.RED +"\nkindly add lowercase letters to your password ")
        UserEntry()
        return False

    if not re.search( "[0-9]", user):
        print(Fore.RED +"\nkindly add digits to your password")
        UserEntry()
        return False

    if not re.search("[#?!@$%^&*-]", user):
        print(Fore.RED +"\nKindly add special character (#?!@$%^&*-)")
        UserEntry()
        return False

    else:
        Password_validation(user)
        print("Valid")
        save()


def save():

    print(Fore.GREEN +"Saving", end="")
    for n in range (0, 10):
        print(Fore.GREEN +">", end="")
        time.sleep(0.3)

    print("\nPassword saved successfully  ")



def Password_validation(user = None):
    userX = input("\nKindly enter password again: ")


    while user != userX:
        print(Fore.RED + "\nPassword don't match, please try again ")
        UserEntry()
        Password_validation()




if __name__ == "__main__":
    UserEntry()
