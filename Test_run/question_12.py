def check_in_len():
    num = int(input("enter num: "))
    user = input("enter word: ")
    if len(user) < 2:
        print(f"{user} " * num)
    else:
        print(user)


if __name__ == '__main__':
    check_in_len()
