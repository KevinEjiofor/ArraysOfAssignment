def greatest():
    return
    largest = 0
    smallest = 10000000000000000000000000000000000000000000000000000000000000000000000000000000
    for number in range(1, 6):
        num = int(input("Enter number: "))

        if num > largest:
            largest = num

        if num < smallest:
            smallest = num


    # print(f"""largest = {largest}
    #         smallest ={smallest}""")


greatest()