counter = 1
total = 0
product = 0
average = 0
largest_number = 0
smallest_number = 100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
while counter <= 4:
    num = int(input("Enter number: "))
    total = total + num

    product = num * num * num * num

    average = total/counter

    counter = counter + 1

    if num > largest_number:
        largest_number = num

    if num < smallest_number:
         smallest_number = num

print(f"""
    sum = {total}
    product = {product}
    average = {average}
    largest number = {largest_number}
    smallest number = {smallest_number}
    """)