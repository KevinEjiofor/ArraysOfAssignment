for number in range(1, 13):
    for numbers in range(1, 13):
        print('%i * %i = %-5i' % (numbers, number, number * numbers), end="\t\t")
    print("\n")

