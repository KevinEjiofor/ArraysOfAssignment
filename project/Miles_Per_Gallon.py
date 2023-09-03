all_mile = 0
all_gallon = 0

gallon = float(input("Enter the gallons used (-1 to end): "))
while gallon != -1:
    mile = float(input("Enter the miles driven: "))
    total = mile / gallon

    print("The miles/gallon for this tank was", total)

    all_mile += mile
    all_gallon += gallon

    gallon = float(input("Enter the gallons used (-1 to end): "))

print(f"The overall average mile/gallon was: {all_mile/all_gallon}")


