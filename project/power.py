entry = 0
while entry <= 8:
    user_password = input("Enter password: ")
    entry = len(user_password)
    if entry < 8:
        print("Password is too short")
print("*" * entry)
print("your password is secured,the length: ", entry)