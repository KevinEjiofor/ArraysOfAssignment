card_valid = " "
card_type = " "
cardN = 0
def card(card_digits):
    global card_type


    if card_digits[0] == 4:
        return "Visa Card"
    elif card_digits[0] == 5:
         return "Master Card"
    elif card_digits[0] == 3 and card_digits[1] == 7:
        return "American Express cards"
    elif card_digits[0] == 6:
        return "Discover cards"
    else:
        return "Unknown"
def card_validate(card_digit):
    total = 0

    for i in range(len(card_digit) - 1, -1, -1):
        if i % 2 == 0:
            digit = card_digit[i] * 2
            total += digit if digit < 10 else digit - 9
        else:
            total += card_digit[i]
    return "Valid" if total % 10 == 0 else "Invalid"



def Application():
    global card_type ,is_valid , cardN
    card_number = input("\nHello, Kindly Enter card details to verify: ")
    card_number = card_number.strip()
    if card_number.isdigit():
        card_digits = list(map(int, card_number))
        if 13 <= len(card_digits) <= 16:
            is_valid = card_validate(card_digits)
            if is_valid == "Valid":
                card_type = card(card_digits)
                cardN = card_number
                display()
            else:
                cardN = card_number
                display_null_card()


        else:
            print("Card number length is not correct")
            Application()
    else:
        print("Invalid entry")
        Application()

def display():
    global card_type,is_valid,cardN
    print("*" * 50)
    print(f"**Credit card Type: {card_type}")
    print(f"**Credit Card Number: {cardN}")
    print(f"**Credit Card Digit length: {len(cardN)}")
    print(f"**Credit Card Validity Status: {is_valid}")
    print("*" * 50)

def display_null_card():
    global card_type, is_valid, cardN
    print("*" * 50)
    print("**Credit card Type: NULL")
    print(f"**Credit Card Number: {cardN}")
    print(f"**Credit Card Digit length: {len(cardN)}")
    print(f"**Credit Card Validity Status: {is_valid}")
    print("*" * 50)




if __name__ == "__main__":
    Application()