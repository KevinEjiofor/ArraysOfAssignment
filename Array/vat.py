vat = 0
user = 0

def user_entry():

    global vat, user
    while True:
        try:
            user_input = input("kindly enter amount: ")
            if not user_input.isdigit():
                print("Enter amount in  digits")
                continue

            elif user_input < "0":
                print("don't enter anything less than 0")
                continue


            vat_input = input("kindly enter Value Added Tax (VAT): ")
            if not vat_input.isdigit():
                print("Enter VAT in digits")
                continue

            elif vat_input <= "0":
                print("don't enter anything less than 0")
                continue

            else:
                user= float(user_input)
                vat = float(vat_input)
                your_vat()

        except(SyntaxError, ValueError ):
            print("invalid entry")


def your_vat():
    global vat,user
    vat_calculation = vat / 100 * user
    vat_sum = user + vat_calculation

    return print(f"your vat amount: {vat_sum}")




if __name__ == '__main__':
     user_entry()
