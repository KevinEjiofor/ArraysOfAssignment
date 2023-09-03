import re


def change(name):
    return name[::-1]

if __name__ == '__main__':
    user = input("kindly Enter your full name: ")
    if re.search("^(?!$)\D+$", user):
        result = change(user)
        print(result)


    else:
        print("\ninvalid entry")
