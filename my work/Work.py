counter = 0
negative = 0
positive = 0
total = 0.0
average = 0
while True:
    numbers = int(input("Enter an inter integer number or break with 0: "))

    if numbers == 0:
        break
    total = total + numbers
    counter += 1

    if numbers > 0:
        positive += 1

    elif numbers < 0:
        negative += 1

average = (total/counter)
print(f"""
        Total: {total}
         Average: {average}
         Positive number: {positive}
         Negative number:  {negative}""")
