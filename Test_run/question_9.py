def check(user):
    return "THIS IS AN EVEN NUMBER" if user % 2 == 0 else "THIS IS AN ODD NUMBER"

if __name__ == '__main__':
    user_entry = int(input("Enter a number: "))
    result = check(user_entry)
    print(result)