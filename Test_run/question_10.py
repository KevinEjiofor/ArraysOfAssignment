import re
num = 0
name = ""

def entry():
    global name
    user = input("Enter your name: ")
    if re.search("^(?!$)\D+$", user):
        name = user
        entry_number()

    else:
        print("invalid entry")
        entry()



def entry_number():
    global num
    number = int(input("Enter number of times you want it to print: "))
    num = number
    printing()


def printing():
    global name,name
    return print(f"{name} \n"  * num)

if __name__ == '__main__':
    entry()