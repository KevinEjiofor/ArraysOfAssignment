largest_number1 = 0
largest_number2 = 0
counter = 1
for counter in range (10):
    number = int(input("Enter number: "))

    if number > largest_number1:
        largest_number2 = largest_number1
        largest_number1 = number
    elif number > largest_number2 and number != largest_number1:
        largest_number2 = number

print(f"""largest number 1: {largest_number1}
      largest number 2: {largest_number2}""" )

