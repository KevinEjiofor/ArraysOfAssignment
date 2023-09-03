import re
import time


def email_validator():
    valid = []
    counter = 0

    while counter < 5:
        email = input("Kindly enter E-mail address: ")
        if email.startswith(".com") or email.endswith("@"):
            print("wrong entry")

        elif email.startswith(".it"):
            print("wrong entry")

        elif email.startswith(".africa"):
            print("wrong entry")

        elif re.match(r"[^@]+@[^@]+\.[^@]+", email):
            valid.append(email)
            counter += 1
            save()
        elif email.endswith(".com"):
            valid.append(email)
            counter += 1
            save()
        elif email.endswith(".it"):
            valid.append(email)
            counter += 1
            save()
        elif email.endswith(".africa"):
            valid.append(email)
            counter += 1
            save()

    return valid
def save():

    print("Saving", end="")
    for n in range (0, 10):
        print(">", end="")
        time.sleep(.9)

    print("\nPassword saved successfully ")



if __name__ == '__main__':

   validate = email_validator()

print("validate E-mail :  ",validate)






